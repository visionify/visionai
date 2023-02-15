import typer
from rich import print
import docker
from rich.console import Console
from rich import print

import sys
from pathlib import Path
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # visionai/visionai directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

from config import *
from util.docker_utils import *

err_console = Console(stderr=True)


if __name__ == '__main__':
    stop_cmd()
