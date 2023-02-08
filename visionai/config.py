import os
import sys
from pathlib import Path
import json
import requests
from rich import print

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # visionai/visionai directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

# Config file
CONFIG_FOLDER = ROOT / 'config'
CONFIG_FILE = ROOT / 'config' / 'config.json'
SCENARIOS_SCHEMA = ROOT / 'config' / 'scenario-schema.json'
SCENARIOS_URL = "https://raw.githubusercontent.com/visionify/visionai/main/visionai/scenarios/scenarios.json"

# Triton server
TRITON_HTTP_URL = 'http://localhost:8000'
TRITON_GRPC_URL = 'grpc://localhost:8001'

TRITON_SERVER_DOCKER_IMAGE = 'nvcr.io/nvidia/tritonserver:22.12-py3'
TRITON_SERVER_EXEC = 'tritonserver'
TRITON_SERVER_COMMAND = 'tritonserver --model-repository=/models'
TRITON_MODELS_REPO = ROOT / 'models-repo'


# Test stuff
if os.environ.get('VISIONAI_EXEC') == 'visionai':
    VISIONAI_EXEC = 'visionai'
else:
    VISIONAI_EXEC = 'python -m visionai'


def init_config():
    '''
    Set up initial configuration (one-time only)
    '''

    if not os.path.isdir(CONFIG_FOLDER):
        os.makedirs(CONFIG_FOLDER, exist_ok=True)
        print(f'init(): Created config folder: {CONFIG_FOLDER}')

    if not os.path.exists(CONFIG_FILE):
        config_data = {
            'version': '0.1',
            'cameras': []
            }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config_data, f, indent=4)
        print(f'init(): Created camera configuration: {CONFIG_FILE}')

    if not os.path.exists(SCENARIOS_SCHEMA):
        res = requests.get(SCENARIOS_URL)
        with open(SCENARIOS_SCHEMA, 'w') as f:
            json.dump(res.json(), f, indent=4)
        print(f'init(): Created scenario schema: {SCENARIOS_SCHEMA}')

    if not os.path.isdir(TRITON_MODELS_REPO):
        os.makedirs(TRITON_MODELS_REPO, exist_ok=True)
        print(f'init(): Created models repo: {TRITON_MODELS_REPO}')

