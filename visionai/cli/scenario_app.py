import os
import sys
import typer
import time
import json
from typing import List, Dict
from uuid import uuid4
from rich import print, prompt
from rich.progress import track
from pathlib import Path
import requests
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel


FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # visionai/visionai directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

MODELS_REPO = ROOT / 'models-repo'

from config import CONFIG_FILE, SCENARIOS_URL, SCENARIOS_OVERRIDE, TRITON_HTTP_URL
from util.download_models import safe_download_to_folder
from models.triton_client import TritonClient
from scenarios import load_scenario

# scenario app
scenario_app = typer.Typer()

# print primitives
def _scenario_pretty(scenario):
    if scenario is None:
        return Panel('[red]NONE[/red]')

    id = scenario.get('id')
    name = scenario.get('name')

    try:
        version = scenario.get('version')
        overview = scenario.get('overview')[:150] + '...'
        model = scenario.get('models')['latest']['name'] + '-v.' + scenario.get('models')['latest']['version']
        accuracy = scenario.get('models')['latest']['accuracy']
        recall = scenario.get('models')['latest']['recall']
        f1 = scenario.get('models')['latest']['f1']
        datasetSize = scenario.get('models')['latest']['datasetSize']
        docs = scenario.get('docs')
        events = '[b]Events: [/b]' + ' | '.join(scenario.get('events'))
        categories = '[b]Categories: [/b]' + ' | '.join(scenario.get('categories'))
        tags = '[b]Tags: [/b]' + ' | '.join(scenario.get('tags'))
        metrics_txt = f'[magenta]Acc: {accuracy}% | Rec: {recall}% | F1: {f1}%[/magenta]\n' + \
            f'[magenta]Size: {datasetSize} images[/magenta]'
        scenario_txt = f'[blue]{model}[/blue]\n' + \
            f'[grey]{overview}[/grey]\n' + \
            metrics_txt + '\n' +\
            f'[grey]{docs}[/grey]\n' +\
            f'[cyan]{events}[/cyan]\n' + \
            f'[cyan]{categories}[/cyan]\n' +\
            f'[cyan]{tags}[/cyan]'

        return Panel(scenario_txt, title=f'[yellow]{name}[/yellow]', width=60, expand=False)
    except Exception as ex:
        return Panel(f'[red]ERR {name}[/red]')

def get_scenarios() -> List[Dict]:
    '''
    Get all scenarios available in the system
    '''
    if Path(SCENARIOS_OVERRIDE).exists():
        with open(SCENARIOS_OVERRIDE, 'r') as f:
            scenarios = json.load(f)['scenarios']
    else:
        res = requests.get(SCENARIOS_URL)
        scenarios = res.json()['scenarios']
    return scenarios

def print_scenarios(scenarios):
    console = Console()
    scen_pretty = [_scenario_pretty(scen) for scen in scenarios]
    console.print(Panel(Columns(scen_pretty), title='Scenarios'))


@scenario_app.command('list')
def scenario_list():
    '''
    List all scenarios available

    List all scenarios available in the system. This includes scenarios
    that may or maynot be applied to any specific camera.
    '''

    # Get scenarios from server. If override file exists, use that.
    all_scenarios = get_scenarios()
    print_scenarios(all_scenarios)

@scenario_app.command('download')
def scenario_download(
    name: str
    ):
    '''
    Download models for scenarios

    Ex: visionai scenario download ppe-detection  # download ppe-detection scenario
    Ex: visionai scenario download all            # download all configured scenarios for the org
    Ex: visionai scenario download world          # download all available scenarios

    Download models for a given scenario, or download models for
    all scenarios that have been configured.
    '''

    # import TritonClient module
    from models.triton_client import TritonClient

    # Get scenarios from server. If override file exists, use that.
    all_scenarios = get_scenarios()

    models_changed = False
    if name.lower() == 'world':
        print(f'Downloading all available (world) scenarios')
        yN = prompt.Confirm.ask('Are you sure you want to download all scenarios? This may take a lot of space!')
        if yN is True:
            num_scenarios = len(all_scenarios)
            for idx, scen in enumerate(all_scenarios):
                print(f'Downloading {idx+1}/{num_scenarios}...')
                scen_url = scen['models']['latest']['model_url']
                models_changed = safe_download_to_folder(scen_url, MODELS_REPO, overwrite=False)

        else:
            raise typer.Exit()

    elif name.lower() == 'all':
        print(f'Downloading all configured scenarios')
        model_names = set()

        if not os.path.exists(CONFIG_FILE):
            print('No scenarios configured. Please use visionai scenario add first')
            return

        with open(CONFIG_FILE) as f:
            config_data = json.load(f)

        for cam in config_data['cameras']:
            for scen in cam['scenarios']:
                model_names.add(scen['name'])

            for preproc in cam['preprocess']:
                model_names.add(preproc['name'])

        if len(model_names) == 0:
            # No models to download
            print(f'Error: No scenarios configured. Use `visionai scenario add`')

        else:
            # Download requred models
            for scen in all_scenarios:
                scen_name = scen['name']
                scen_url = scen['models']['latest']['model_url']
                if scen_url is None:
                    continue

                if scen_name in model_names:
                    print(f'Model: {scen_name}: {scen_url}')
                    models_changed = safe_download_to_folder(scen_url, MODELS_REPO, overwrite=False)

    else:
        print(f'Downloading models for scenario: {name}')
        download_success = False

        # If a single scenario name is specified.
        for scen in all_scenarios:
            scen_name = scen['name']
            scen_url = scen['models']['latest']['model_url']
            if scen_url is None:
                continue

            if scen_name == name:
                print(f'Model: {scen_name}: {scen_url}')
                models_changed = safe_download_to_folder(scen_url, MODELS_REPO, overwrite=False)
                download_success = True
                break

        if download_success is False:
            print(f'ERROR: Unable to find scenario: {name}')

    # If any new models were downloaded, restart the model server
    if models_changed is True:
        print('Restarting model server...')
        tc = TritonClient()
        tc.stop_model_server()
        tc.start_model_server()
        print('Restarted model server.')

    # Done downloading models.
    print('Done.')


@scenario_app.command('test')
def scenario_test(
    name:str,
    camera: str = typer.Option('0', help='Camera name (default is webcam)')
    ):
    '''
    Run the scenario locally to test it out.

    - Download the model if not available.
    - Pull the model server container image.
    - Start the model server container with this model.
    - Run inference with this model
    '''

    # import TritonClient module
    from models.triton_client import TritonClient

    # Get scenarios from server. If override file exists, use that.
    all_scenarios = get_scenarios()

    scenario_to_test = None
    for scen in all_scenarios:
        if scen['name'] == name:
            scenario_to_test = scen
            break

    if scenario_to_test is None:
        print(f'ERROR: Scenario {name} not found.')
        raise typer.Exit()

    # Check if model server is running
    tc = TritonClient()
    if not tc.is_triton_running():
        print(f'ERROR: Model server is not running. Start with')
        print('[magenta] visionai models serve [/magenta]')
        raise typer.Exit()
    else:
        print('Model-server running.')


    # Check if the specified scenario model is running.
    model_to_test_available = False
    model_name = scenario_to_test['models']['latest']['name']

    model_list = tc.get_models()
    for model_item in model_list:
        if model_item['name'] == model_name:
            model_to_test_available = True
            break

    # Print models being run
    tc.print_models_served()

    if not model_to_test_available:
        print(f'ERROR: Model {name} is not being served by the model-server.')
        print(f'Download models and restart model-server')
        print(f'[magenta]visionai models stop[/magenta]')
        print(f'[magenta]visionai scenario download {name}[/magenta]')
        print(f'[magenta]visionai models serve[/magenta]')
        print(f'[magenta]visionai scenario test {name} [/magenta]')
        raise typer.Exit()
    else:
        print(f'Model {name} is being served.')

    print(f'Loading inference engine for {name}')
    inference_engine = load_scenario(scenario_name=name, camera_name=camera)

    # for test command - block the main thread.
    print(f'Running on default web-cam')
    inference_engine.start()

    #TODO: Provide support for running on any camera


@scenario_app.callback()
def callback():
    '''
    Manage scenarios

    An organization can have multiple scenarios that are installed
    at different places. They may be from different vendors and/or
    maybe using different security surveillance software. Most
    scenarios however do support RTSP, RTMP or HLS streams as an
    output. Please refer to your scenario vendor documentation to
    find this out. This module will help you onboard those scenarios
    on visionai systems by using a simple named instance for each
    scenario.
    '''

if __name__ == '__main__':
    # scenario_app()
    # scenario_list()

    # scenario_remove('smoke-and-fire-detection', 'TEST-999')
    # scenario_add('smoke-and-fire', 'TEST-999')
    # scenario_download(world=True)
    scenario_download('face-blur')

    # scenario_download('all')

    # scenario_test(name='smoke-and-fire-detection', camera=0)

    # scenario_test(name='face-blur', camera=0)
