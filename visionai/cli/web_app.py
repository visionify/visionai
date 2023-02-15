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
web_app = typer.Typer()

@web_app.command('start')
def web_start():
    '''
    Start web server

    Use this function to start the web-service. Web service
    can be used for more intuitive configuration for the
    cameras and scenarios. Web-app is also the place to view
    event details, camera live-stream etc.
    '''
    try:
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - -')

        # Check if already running
        web_app_running = False
        web_api_running = False
        redis_running = False
        grafana_running = False

        client = docker.from_env()
        containers = client.containers.list()
        for container in containers:
            if container.name == WEB_APP_CONTAINER_NAME:
                print(f'Web app available at: http://localhost:{WEB_APP_PORT}')
                web_app_running = True
            if container.name == WEB_API_CONTAINER_NAME:
                print(f'Web service API available at: http://localhost:{WEB_API_PORT}')
                web_api_running = True
            if container.name == REDIS_CONTAINER_NAME:
                print(f'Redis server is at: redis://localhost:{REDIS_SERVER_PORT}')
                redis_running = True
            if container.name == GRAFANA_CONTAINER_NAME:
                print(f'Grafana server is at: http://localhost:{GRAFANA_SERVER_PORT}')
                grafana_running = True

        # If all services are running, return
        if web_app_running and web_api_running and redis_running and grafana_running:
            return

        if web_app_running is False:
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

    except Exception as e:
        err_console.print_exception()
        print(f'Error: {e}')

@web_app.command('stop')
def web_stop(web: str=None):
    '''
    Stop web server

    Use this function to stop already running web-service. There
    can be a single instance of the web-service supported currently.
    So there is no need for any arguments for this function.
    '''
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

        print(f'Done.')

def print_container_status(container_name, tail):
    try:
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print(f'{container_name} status....')
        client = docker.from_env()
        ctainer = client.containers.get(container_name)
        ctainer_status = typer.style(ctainer.status, fg=typer.colors.WHITE, bg=typer.colors.GREEN)
        typer.echo(ctainer_status)
        logs = ctainer.logs(tail=tail)
        log_message= logs.decode("utf-8")
        print(log_message)
        web_service_port_message = typer.style(ctainer.ports, fg=typer.colors.WHITE, bg=typer.colors.GREEN)
        typer.echo(web_service_port_message)
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - -')

    except docker.errors.NotFound:
        message = typer.style(f"{container_name} not running", fg=typer.colors.WHITE, bg=typer.colors.RED)
        typer.echo(message)

@web_app.command('status')
def web_status(
    tail: int = typer.Option(20, help='tail number of lines')
    ):
    '''
    Web service status

    Use this function to get the status of the web-service. (if
    its running or not. This function also prints diagnostic
    information like last few log messages etc.)
    '''
    print_container_status(WEB_APP_CONTAINER_NAME, tail)
    print_container_status(WEB_API_CONTAINER_NAME, tail)
    print_container_status(REDIS_CONTAINER_NAME, tail)
    print_container_status(GRAFANA_CONTAINER_NAME, tail)


@web_app.callback()
def callback():
    '''
    Start/stop web-app

    Start and stop the VisionAI web-app which can be a more
    intuitive way of managing cameras, pipelines and scenarios.
    Web-app also provides a live-stream view of the cameras.
    '''
    pass

if __name__ == '__main__':
    # web_app()

    web_stop()