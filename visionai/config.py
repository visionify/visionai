import os
import sys
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # visionai/visionai directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

# Config file
CONFIG_FILE = ROOT / 'config' / 'config.json'
SCENARIOS_SCHEMA = ROOT / 'config' / 'scenario-schema.json'
# SCENARIOS_URL = "https://raw.githubusercontent.com/visionify/visionai-scenarios/main/scenarios.json"
SCENARIOS_URL = "F:\\visionify\\visionai\\visionai\\config\\scenario-schema.json"
# Triton server
TRITON_HTTP_URL = 'localhost:8000'
TRITON_SERVER_DOCKER_IMAGE = 'nvcr.io/nvidia/tritonserver:22.12-py3'
TRITON_SERVER_EXEC = 'tritonserver'
TRITON_SERVER_COMMAND = 'tritonserver --model-repository=/models'
TRITON_MODELS_REPO = ROOT / 'models-repo'


# Test stuff
if os.environ.get('VISIONAI_EXEC') == 'visionai':
    VISIONAI_EXEC = 'visionai'
else:
    VISIONAI_EXEC = 'python -m visionai'

