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
from models.triton_client import TritonClient

err_console = Console(stderr=True)
tc = TritonClient()

def stop_cmd():
    try:
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print(f'Stop web-app....')
        client = docker.from_env()
        web_service_container = client.containers.get(WEB_APP_CONTAINER_NAME)
        web_service_container.stop()
    except docker.errors.NotFound :
        message = typer.style(f"Web-app not running", fg=typer.colors.WHITE, bg=typer.colors.RED)
        typer.echo(message)

    try:
        print(f'Stop API service....')
        web_api_container = client.containers.get(WEB_API_CONTAINER_NAME)
        web_api_container.stop()
    except docker.errors.NotFound :
        message = typer.style(f"Web-API not running", fg=typer.colors.WHITE, bg=typer.colors.RED)
        typer.echo(message)

    try:
        print(f'Stop redis server....')
        redis_container = client.containers.get(REDIS_CONTAINER_NAME)
        redis_container.stop()
    except docker.errors.NotFound :
        message = typer.style(f"Redis not running", fg=typer.colors.WHITE, bg=typer.colors.RED)
        typer.echo(message)

    try:
        print(f'Stop grafana server....')
        grafana_container = client.containers.get(GRAFANA_CONTAINER_NAME)
        grafana_container.stop()
    except docker.errors.NotFound :
        message = typer.style(f"Grafana not running", fg=typer.colors.WHITE, bg=typer.colors.RED)
        typer.echo(message)

    try:
        print(f'Stop Triton server....')
        tc.stop_model_server()
    except docker.errors.NotFound :
        message = typer.style(f"Triton not running", fg=typer.colors.WHITE, bg=typer.colors.RED)
        typer.echo(message)

    print(f'Done.')

def print_container_status(container_name, tail):
    try:
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print(f'{container_name} status....')
        client = docker.from_env()
        ctainer = client.containers.get(container_name)
        ctainer_status = typer.style(ctainer.status, fg=typer.colors.WHITE, bg=typer.colors.GREEN)
        typer.echo(f"{container_name}: {ctainer_status}")
        logs = ctainer.logs(tail=tail)
        log_message= logs.decode("utf-8")
        print(log_message)
        web_service_port_message = typer.style(json.dumps(ctainer.ports), fg=typer.colors.WHITE, bg=typer.colors.GREEN)
        typer.echo(web_service_port_message)
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - -')

    except docker.errors.NotFound:
        message = typer.style(f"{container_name} not running", fg=typer.colors.WHITE, bg=typer.colors.RED)
        typer.echo(message)

def status_cmd(
    tail: int = typer.Option(20, help='tail number of lines')
    ):
    print_container_status(WEB_APP_CONTAINER_NAME, tail)
    print_container_status(WEB_API_CONTAINER_NAME, tail)
    print_container_status(REDIS_CONTAINER_NAME, tail)
    print_container_status(GRAFANA_CONTAINER_NAME, tail)
    print_container_status(TRITON_SERVER_CONTAINER_NAME, tail)


def init_cmd():
    try:
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - -')

        # Package dependencies:
        # opencv-python = "^4.6.0"
        # torch = "^1.11.0"
        # torchvision = ">=0.12,<0.15"
        # pandas = "^1.3.5"
        # seaborn = ">=0.11.2,<0.13.0"
        # tritonclient = {extras = ["all"], version = "^2.29.0"}
        check_requirements(['opencv-python', 'torch', 'torchvision', 'pandas', 'seaborn', 'tritonclient[all]'], install=True)

        # Check if already running
        init_app_running = False
        web_api_running = False
        redis_running = False
        grafana_running = False
        triton_running = False

        client = docker.from_env()
        containers = client.containers.list()
        for container in containers:
            if container.name == WEB_APP_CONTAINER_NAME:
                print(f'Web server already running at: http://localhost:{WEB_APP_PORT}')
                init_app_running = True
            if container.name == WEB_API_CONTAINER_NAME:
                print(f'API server already running at: http://localhost:{WEB_API_PORT}')
                web_api_running = True
            if container.name == REDIS_CONTAINER_NAME:
                print(f'Redis server is at: localhost:{REDIS_SERVER_PORT}')
                redis_running = True
            if container.name == GRAFANA_CONTAINER_NAME:
                print(f'Grafana server is at: http://localhost:{GRAFANA_SERVER_PORT}')
                grafana_running = True
            if container.name == TRITON_SERVER_CONTAINER_NAME:
                print(f'Triton http server is at: {TRITON_HTTP_URL}')
                print(f'Triton grpc server is at: {TRITON_GRPC_URL}')
                print(f'Triton prometheus metrics server is at: {TRITON_METRICS_URL}')
                triton_running = True

        # If all services are running, return
        if init_app_running and web_api_running and redis_running and grafana_running:
            return

        if init_app_running is False:
            print(f'Starting web app at port {WEB_APP_PORT}')
            docker_container_start(
                container_name=WEB_APP_CONTAINER_NAME,
                image=WEB_APP_DOCKER_IMAGE,
                portmap={80:WEB_APP_PORT},
                network_name=DOCKER_NETWORK
            )
            print(f'Web app available at: http://localhost:{WEB_APP_PORT}')

        if web_api_running is False:
            print(f'Starting web service API at port {WEB_API_PORT}')

            if sys.platform == 'win32':
                DOCKER_SOCK = '//var/run/docker.sock'
            else:
                DOCKER_SOCK = '/var/run/docker.sock'

            docker_container_start(
                container_name=WEB_API_CONTAINER_NAME,
                image=WEB_API_DOCKER_IMAGE,
                portmap={3002:WEB_API_PORT},
                network_name=DOCKER_NETWORK,
                volmap=[
                    f'{WEB_API_MODELS_REPO}:/models',
                    f'{WEB_API_CONFIG_FOLDER}:/config',
                    f'{DOCKER_SOCK}:/var/run/docker.sock'
                ],
                command='python server.py --models-repo /models --config /config'
            )
            print(f'Web service API available at: http://localhost:{WEB_API_PORT}')

        if redis_running is False:
            print(f'Starting redis server at port {REDIS_SERVER_PORT}')
            redis_container_start()
            redis_python_install()
            print(f'Redis server is at: redis://localhost:{REDIS_SERVER_PORT}')

        if grafana_running is False:
            print(f'Starting grafana server at port {GRAFANA_SERVER_PORT}')
            grafana_container_start()
            print(f'Grafana server is at: http://localhost:{GRAFANA_SERVER_PORT}')

        if triton_running is False:
            print(f'Starting triton server..')
            tc.start_model_server()
            print(f'Triton http server is at: {TRITON_HTTP_URL}')
            print(f'Triton grpc server is at: {TRITON_GRPC_URL}')
            print(f'Triton prometheus metrics server is at: {TRITON_METRICS_URL}')

    except Exception as e:
        err_console.print_exception()
        print(f'Error: {e}')



if __name__ == '__main__':
    # init_cmd()
    # stop_cmd()
    status_cmd()
