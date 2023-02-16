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
SCENARIOS_URL = "https://raw.githubusercontent.com/visionify/visionai/main/visionai/scenarios/scenarios.json"
SCENARIOS_OVERRIDE = ROOT / 'config' / 'scenarios-override.json'

# Triton server endpoints
TRITON_HTTP_URL = 'http://localhost:8000'
TRITON_GRPC_URL = 'grpc://localhost:8001'
TRITON_METRICS_URL = 'http://localhost:8002/metrics'

TRITON_SERVER_CONTAINER_NAME = 'visionai-triton'
TRITON_SERVER_DOCKER_IMAGE = 'nvcr.io/nvidia/tritonserver:22.12-py3'
TRITON_SERVER_EXEC = 'tritonserver'
TRITON_SERVER_COMMAND = 'tritonserver --model-repository=/models'
TRITON_MODELS_REPO = ROOT / 'models-repo'

# Redis server configuration
REDIS_ENABLED = True
REDIS_SERVER_DOCKER_IMAGE = 'redis'
REDIS_SERVER_PORT = 6379
REDIS_CONTAINER_NAME = 'visionai-redis'

# Grafana server configuration
GRAFANA_ENABLED = True
GRAFANA_SERVER_DOCKER_IMAGE = 'grafana/grafana'
GRAFANA_SERVER_PORT = 3003
GRAFANA_CONTAINER_NAME = 'visionai-grafana'
GRAFANA_DATA_DIR = ROOT / 'config' / 'grafana-data'
GRAFANA_PROVISIONING_DIR = ROOT / 'config' / 'grafana-provisioning'

# Web application (front-end)
WEB_APP_DOCKER_IMAGE = 'visionify/visionaiweb'
WEB_APP_PORT = 3001
WEB_APP_CONTAINER_NAME = 'visionai-web'

# Web API (back-end)
WEB_API_DOCKER_IMAGE = 'visionify/visionai-api'
WEB_API_PORT = 3002
WEB_API_MODELS_REPO = ROOT / 'models-repo'
WEB_API_CONFIG_FOLDER = ROOT / 'config'
WEB_API_CONTAINER_NAME = 'visionai-api'

# Docker network
DOCKER_NETWORK = 'visionai-network'

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

    if not os.path.isdir(TRITON_MODELS_REPO):
        os.makedirs(TRITON_MODELS_REPO, exist_ok=True)
        print(f'init(): Created models repo: {TRITON_MODELS_REPO}')


    if GRAFANA_ENABLED:
        if not os.path.isdir(GRAFANA_DATA_DIR):
            os.makedirs(GRAFANA_DATA_DIR, exist_ok=True)
            print(f'init(): Created Grafana data directory: {GRAFANA_DATA_DIR}')

        if not os.path.isdir(GRAFANA_PROVISIONING_DIR):
            os.makedirs(GRAFANA_PROVISIONING_DIR, exist_ok=True)
            print(f'init(): Created Grafana provisioning directory: {GRAFANA_PROVISIONING_DIR}')
