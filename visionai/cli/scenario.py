import os
import sys
import typer
import time
import json
from uuid import uuid4
from rich import print, prompt
from rich.progress import track
from pathlib import Path
import requests

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # visionai/visionai directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

MODELS_REPO = ROOT / 'models-repo'

from config import CONFIG_FILE, SCENARIOS_SCHEMA, SCENARIOS_URL
from util.download_models import safe_download_to_folder

scenario_app = typer.Typer()

# scenario app
@scenario_app.command('list-all')
def scenario_all():
    '''
    List all scenarios available

    List all scenarios available in the system. This includes scenarios
    that may or maynot be applied to any specific camera.
    '''
    try:
        res = requests.get(SCENARIOS_URL)
        # with open(SCENARIOS_SCHEMA, 'w') as f:
        #     json.dump(res.json(), f, indent=4)

        scenarios = res.json()['scenarios']
    except Exception as ex:
        scenarios = str(ex)

    print(scenarios)

@scenario_app.command('list')
def scenario_list(
    camera = typer.Option(None, help="Camera name")
):
    '''
    List scenarios configured for a camera

    This method only lists scenarios configured for a given camera, or
    if no camera name is provided - it would list all scenarios available
    in the system.
    '''
    # Camera is available in system
    camera_scenarios = None
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config_data = json.load(f)
        for cam in config_data['cameras']:
            if cam['name'] == camera:
                camera_scenarios = cam['scenarios']
                break

    # Camera is available in system
    if camera_scenarios is not None:
        print(f'Listing configured scenarios for: {camera}')
        print(camera_scenarios)

    else:
        print(f'Listing all available scenarios')
        scenario_all()



@scenario_app.command('add')
def scenario_add(
    scenario: str = typer.Option(..., help='scenario name', prompt=True),
    camera: str = typer.Option(..., help='camera name', prompt=True)
    ):
    '''
    Add a scenario to be run for a camera

    Add an individual scenario to be run for a camera. Specify the
    names for scenario and camera.
    '''

    print(f'Adding scenario : {scenario} for camera: {camera}')
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config_data = json.load(f)

    else:
        config_data = {
            'version': '0.1',
            'cameras': []
            }

    # find camera
    found_camera = False
    for cam in config_data['cameras']:
        if cam['name'] == camera:
            found_camera = True

            scen_already_present = False
            for scen in cam['scenarios']:
                if scen['name'] == scenario:
                    scen_already_present = True
                    break

            if scen_already_present is False:
                cam['scenarios'].append({
                    'name': scenario,
                    'events': 'all',
                    'schedule': 'all',
                    'focus': 'all'
                })

                with open(CONFIG_FILE, 'w') as f:
                    json.dump(config_data, f, indent=4)

                print(f'Scenario {scenario} successfully added for camera {camera}')

            else:
                print(f'Scenario {scenario} already present for camera {camera}')

            break

    if not found_camera:
        print(f'Error: camera {camera} not available')
        return


@scenario_app.command('remove')
def scenario_remove(
    scenario: str=typer.Option(..., help='scenario name', prompt=True),
    camera: str=typer.Option(..., help='camera', prompt=True)
    ):
    '''
    Remove a scenario from the system

    Specify a named scenario that needs to be removed from
    the system. Once removed, all the scenarios and pre-process
    routines associated with the scenario will be removed.
    '''

    print(f'Removing scenario : {scenario} from camera {camera}')
    if not os.path.exists(CONFIG_FILE):
        print('No scenarios available in the system. Exiting.')
        return

    with open(CONFIG_FILE, 'r') as f:
        config_data = json.load(f)

    # Check if name already present
    found = False
    for cam in config_data['cameras']:
        for scen in cam['scenarios']:
            if scen['name'] == scenario:
                found = True
                cam['scenarios'].remove(scen)
                break

    if found:
        # Write back to JSON if successfully removed.
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config_data, f, indent=4)

        print(f'Successfully removed scenario: {scenario} from {camera}')
    else:
        print(f'Unable to remove scenario {scenario} from {camera}')

@scenario_app.command('download')
def scenario_download(
    scenario: str=typer.Option('all', help='scenario name'),
    world: bool=typer.Option(False, help='Download all public scenarios available')
    ):
    '''
    Download models for scenarios

    all - all scenarios configured for cameras in this system.
    world - all available public scenarios (this might take a lot of space.)
    individual - specify scenario name you want to download.

    Download models for a given scenario, or download models for
    all scenarios that have been configured.
    '''

    print(f'Downloading scenarios : {scenario}')

    # Get list of available scenarios.
    # res = requests.get(SCENARIOS_URL)
    with open(SCENARIOS_URL, 'r') as f:
        res = json.load(f)
    all_scenarios = res['scenarios']


    if world == True:
        yN = prompt.Confirm.ask('Are you sure you want to download all scenarios? This may take a lot of space!')
        if yN is True:
            num_scenarios = len(all_scenarios)
            for idx, scen in enumerate(all_scenarios):
                print(f'Downloading {idx+1}/{num_scenarios}...')
                scen_url = scen['models']['latest']['model_url']
                safe_download_to_folder(scen_url, MODELS_REPO)
        else:
            raise typer.Exit()

    if scenario == 'all':
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
                    safe_download_to_folder(scen_url, MODELS_REPO)

    else:
        # If a single scenario name is specified.
        for scen in all_scenarios:
            scen_name = scen['name']
            scen_url = scen['models']['latest']['model_url']
            if scen_url is None:
                continue

            if scen_name == scenario:
                print(f'Model: {scen_name}: {scen_url}')
                safe_download_to_folder(scen_url, MODELS_REPO)
                break

    # Done downloading models.
    print('Done.')

@scenario_app.command('preview')
def scenario_preview(
    name:str = typer.Option(..., help='scenario name to preview')
    ):
    '''
    Preview the scenario feed

    View the scenario feed, review FPS etc available for scenario.
    '''
    print(f"TODO: Implement scenario preview functionality.")

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

    # scenario_remove('smoke-and-fire-detection', 'TEST-999')
    # scenario_add('smoke-and-fire', 'TEST-999')
    scenario_download(world=True)
    # scenario_add('slip-and-fall', '0')
    # scenario_list()
