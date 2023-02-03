import os
import sys
import typer
import time
import json
from uuid import uuid4
from rich import print
from rich.progress import track
from pathlib import Path
import cv2

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
    if not os.path.exists(CONFIG_FILE):
        print('No cameras available in the system')

    else:
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
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config_data = json.load(f)

        # Check if name already present
        for camera in config_data['cameras']:
            if camera['name'] == name:
                print(f'Error: Camera {name} already present')
                return

        # TODO: Maybe validate URI string also later.
    else:
        config_data = {
            'version': '0.1',
            'cameras': []
            }

    # TODO: Validate the camera stream is good (check FPS)
    config_data['cameras'].append({
        'id': str(uuid4()),
        'name': name,
        'uri': uri,
        'events': 'all',
        'preprocess': [],
        'scenarios': []
    })

    with open(CONFIG_FILE, 'w') as f:
        json.dump(config_data, f, indent=2)

    print('Successfully added camera.')


@camera_app.command('remove')
def camera_remove(name: str=typer.Option('Camera name', prompt=True, confirmation_prompt=True)):
    '''
    Remove a camera from the system

    Specify a named camera that needs to be removed from
    the system. Once removed, all the scenarios and pre-process
    routines associated with the camera will be removed.
    '''

    print(f'Removing camera : {name}')
    if not os.path.exists(CONFIG_FILE):
        print('No cameras available in the system. Exiting.')
        return

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


@camera_app.command('preview')
def camera_preview(
    name:str = typer.Option(..., help='camera name to preview')
    ):
    '''
    Preview the camera system

    View the camera feed, review FPS etc available for camera.
    '''
    print(f"TODO: Implement camera preview functionality.")
    # with open(CONFIG_FILE, 'r') as f:
    #     config_data = json.load(f)
    #     # cam_uri = config_data['cameras'][0]['uri']
    #     vid = cv2.VideoCapture(0)
    #     while(True):
    #         ret, frame = vid.read()
    #         cv2.resize(frame, (240,240))
    #         cv2.imshow('frame', frame)
    #         if cv2.waitKey(1) & 0xFF == ord('q'):
    #             break
    #     vid.release()
    #     cv2.destroyAllWindows()

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
    # camera_app()
    camera_add('0', '0', 'my_webcam')
    # camera_remove('TEST-999')