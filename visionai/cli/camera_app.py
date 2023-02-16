import os
import sys
import typer
import time
import json
from uuid import uuid4
from rich import print
from rich.progress import track
from rich.prompt import Prompt
from pathlib import Path
import datetime

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # visionai/visionai directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

from config import CONFIG_FILE

camera_app = typer.Typer()

# Camera app
@camera_app.command('list')
def camera_list():
    '''
    List available cameras

    Print cameras available in the system and the scenarios / routines
    that are set up for them.
    '''
    with open(CONFIG_FILE, 'r') as f:
        config_data = json.load(f)
    print(config_data['cameras'])

@camera_app.command('add')
def camera_add(
    name: str = typer.Option(..., help='Camera Name', prompt=True),
    uri: str = typer.Option(..., help='URI for camera', prompt=True),
    description: str = typer.Option(..., help='Description', prompt=True)
    ):
    '''
    Add a named camera instance

    Add a camera as a named instance in the system. For adding
    a camera we support RTSP, HLS, HTTP(S) systems. To add a camera
    you need to provide a name for the camera, URI for the camera
    (including any username/password within the URI itself),
    description for camera (about its location, where its pointing,
    who is the vendor etc.).

    Before the camera is added - we need to test out if the
    camera instance is valid. We need to be able to read from
    the camera and calculate its FPS. Show this information
    on the screen.
    '''

    print(f'Adding camera : {name}, {uri}, {description}')
    with open(CONFIG_FILE, 'r') as f:
        config_data = json.load(f)

    # Check if name already present
    for camera in config_data['cameras']:
        if camera['name'] == name:
            print(f'Error: Camera {name} already present')
            return

    # TODO: Validate the camera stream is good (check FPS)
    config_data['cameras'].append({
        'id': str(uuid4()),
        'name': name,
        'uri': uri,
        'events': 'all',
        'description': description,
        'preprocess': [],
        'scenarios': []
    })

    with open(CONFIG_FILE, 'w') as f:
        json.dump(config_data, f, indent=2)

    print(f'Successfully added camera: {name}')


@camera_app.command('remove')
def camera_remove(name: str=typer.Option('Camera name', prompt=True, confirmation_prompt=True)):
    '''
    Remove a camera from the system

    Specify a named camera that needs to be removed from
    the system. Once removed, all the scenarios and pre-process
    routines associated with the camera will be removed.
    '''

    print(f'Removing camera : {name}')
    with open(CONFIG_FILE, 'r') as f:
        config_data = json.load(f)

    # Check if name already present
    found = False
    for camera in config_data['cameras']:
        if camera['name'] == name:
            found = True
            config_data['cameras'].remove(camera)
            break

    if found:
        # Write back to JSON if successfully removed.
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config_data, f, indent=4)

        print(f'Successfully removed camera: {name}')
    else:
        print(f'Unable to find camera {name} to remove')

@camera_app.command('reset')
def camera_reset(
    confirm: bool=typer.Option(False, help="Confirm delete", prompt="Are you sure you want to reset camera configuration?")
):
    '''
    Reset all camera configuration.

    All cameras and their scenarios would be removed
    from the system. Any earlier configuration is backed up
    as a timed json backup file.
    '''

    if confirm is True:
        print('Deleting all camera configuration')
        with open(CONFIG_FILE, 'r') as f:
            config_data = json.load(f)

        backup_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        with Path(CONFIG_FILE).with_suffix(f'.{backup_time}.backup.json') as backup_file:
            if len(config_data['cameras']) > 0:
                print(f'Backing up current camera configuration at: {backup_file}')
                with open(backup_file, 'w') as f:
                    json.dump(config_data, f, indent=4)

        with open(CONFIG_FILE, 'w') as f:
            config_data = {
                'version': '0.1',
                'cameras': []
                }
            json.dump(config_data, f, indent=4)
        print('Camera configuration reset.')

    else:
        print('Skip resetting camera configuration')

@camera_app.command('preview')
def camera_preview(
    name:str = typer.Option(..., help='camera name to preview')
    ):
    '''
    Preview the camera system

    View the camera feed, review FPS etc available for camera.
    '''
    print(f"TODO: Implement camera preview functionality.")

@camera_app.command('add-scenario')
def camera_add_scenario(
    camera: str = typer.Option(..., help='camera name', prompt=True),
    scenario: str = typer.Option(..., help='scenario name', prompt=True)
    ):
    '''
    Add a scenario for a camera

    Add an individual scenario to be run for a camera. Specify the
    names for scenario and camera.
    '''

    print(f'Adding scenario : {scenario} for camera: {camera}')
    with open(CONFIG_FILE, 'r') as f:
        config_data = json.load(f)

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


@camera_app.command('list-scenarios')
def camera_list_scenarios(
    camera: str = typer.Option(..., help='camera name', prompt=True)
    ):
    '''
    List scenarios for a camera

    List all the scenarios for a camera. Specify the
    names for scenario and camera.
    '''

    print(f'Listing scenarios for camera: {camera}')
    with open(CONFIG_FILE, 'r') as f:
        config_data = json.load(f)

    # find camera
    found_camera = False
    for cam in config_data['cameras']:
        if cam['name'] == camera:
            found_camera = True

            if len(cam['scenarios']) > 0:
                print(f'Available scenarios for camera {camera}:')
                for scen in cam['scenarios']:
                    print(f'  {scen["name"]}')
            else:
                print(f'No scenarios available for camera {camera}')

            break

    if not found_camera:
        print(f'Error: camera {camera} not available')
        return


@camera_app.command('remove-scenario')
def scenario_remove(
    camera: str=typer.Option(..., help='camera', prompt=True),
    scenario: str=typer.Option(..., help='scenario name', prompt=True)
    ):
    '''
    Remove a scenario from a camera

    Specify a named scenario that needs to be removed from
    the system. Once removed, all the scenarios and pre-process
    routines associated with the scenario will be removed.
    '''

    print(f'Removing scenario : {scenario} from camera {camera}')
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


@camera_app.command('list-scenario')
@camera_app.command('list-scenarios')
def scenario_list(
    camera:str = typer.Option('', help="Camera name")
):
    '''
    List scenarios configured for a camera

    '''
    with open(CONFIG_FILE, 'r') as f:
        config_data = json.load(f)

    # if no camera provided, print scenarios for all cameras.
    if camera == '':
        scenarios_list = []
        for cam in config_data['cameras']:
            scenarios_list.append({
                'cam': cam['name'],
                'scenarios': cam['scenarios']
            })

        print(f'scenarios for all cameras:')
        print(scenarios_list)

    else:
        camera_found = False
        scenarios_list = []
        for cam in config_data['cameras']:
            if cam['name'] == camera:
                camera_found = True
                scenarios_list.append({
                    'cam': camera,
                    'scenarios': cam['scenarios']
                })
                break
        if camera_found:
            print(f'scenarios for camera: {camera}')
            print(scenarios_list)
        else:
            print(f'camera not found: {camera}')


@camera_app.callback()
def callback():
    '''
    Manage cameras

    An organization can have multiple cameras that are installed
    at different places. They may be from different vendors and/or
    maybe using different security surveillance software. Most
    cameras however do support RTSP, RTMP or HLS streams as an
    output. Please refer to your camera vendor documentation to
    find this out. This module will help you onboard those cameras
    on visionai systems by using a simple named instance for each
    camera.
    '''

if __name__ == '__main__':
    camera_app()

