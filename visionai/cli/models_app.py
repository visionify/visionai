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

from config import CONFIG_FILE, SCENARIOS_URL, TRITON_SERVER_DOCKER_IMAGE
from util.general import invoke_cmd
from util.download_models import safe_download_to_folder
from models.triton_client import TritonClient

# Model serve app
models_app = typer.Typer()

@models_app.command('check')
def models_check():
    '''
    Check model-server status & print helpful debug info.

    TODO:
    Goal of the check command is to identify any configuration/dependency
    issues that we can inform to user that he can fix on his end. This could
    be like missing dependency, missing software package, missing driver details
    etc.

    - Check if model-server is running or not.
    - Check if triton-client can access model-server
    - Check what are the models served
    - Print all of this in a pretty manner [checkbox based]
    - Check container logs & show them here.
    - grep container logs for common errors & highlight that in output
    '''
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print('Checking model server...')

    # TODO: may need other information for debug
    #
    tc = TritonClient()
    tc.print_models_served()

@models_app.command('start')
@models_app.command('serve')
def models_start():
    '''
    Start serving all available models.

    All models present in the models-repo/ will be served. We use
    triton inference server to serve them. The triton server will be
    at http://localhost:8000, grpc://localhost:8001.

    Please make sure these two ports are not used by anyone else.
    '''
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print('Start models...')
    tc = TritonClient()
    tc.start_model_server()
    tc.print_models_served()

@models_app.command('stop')
def models_stop():
    '''
    Stop serving all models.

    This method will stop serving all models. Any inference running
    will all be stopped as well.
    '''
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print('Stop models...')
    tc = TritonClient()
    tc.stop_model_server()

@models_app.command('list')
@models_app.command('status')
def models_status():
    '''
    Show the status of serving models

    Shows how many models are being served, metrics for the models etc.
    '''
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print('Models status...')
    tc = TritonClient()
    tc.print_models_served()

@models_app.callback()
def callback():
    '''
    Serve models

    Before we can run any scenarios - the models necessary for them
    must be ready. We use Triton inference server to make the
    best use of GPU/CPU resources available on the machine in order
    to serve our models. Any models that are available in
    models-repo folder would be served after this (TODO - only
    serve models configured in scenarios).
    '''

if __name__ == '__main__':
    # models_app()

    models_status()

