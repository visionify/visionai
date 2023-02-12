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

from config import WEB_APP_DOCKER_IMAGE, WEB_APP_PORT, WEB_APP_CONTAINER_NAME
from config import WEB_API_DOCKER_IMAGE, WEB_API_PORT, WEB_API_MODELS_REPO, WEB_API_CONFIG_FOLDER, WEB_API_CONTAINER_NAME

from util.docker_utils import docker_image_pull_with_progress

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
        client = docker.from_env()
        containers = client.containers.list()
        web_app_running = False
        web_api_running = False
        for container in containers:
            if container.name == WEB_APP_CONTAINER_NAME:
                print(f'Web server already running at: http://localhost:{WEB_APP_PORT}')
                web_app_running = True
            if container.name == WEB_API_CONTAINER_NAME:
                print(f'API server already running at: http://localhost:{WEB_API_PORT}')
                web_api_running = True

        # If already running, return
        if web_app_running and web_api_running:
            return

        # If images are not pulled first, pull them first.
        try:
            web_app_image = client.images.get(WEB_APP_DOCKER_IMAGE)
        except docker.errors.ImageNotFound:
            print(f'{WEB_APP_DOCKER_IMAGE} not found locally')
            print(f"Pulling web-app image {WEB_APP_DOCKER_IMAGE}....")
            docker_image_pull_with_progress(client, WEB_APP_DOCKER_IMAGE)

        try:
            web_api_image = client.images.get(WEB_API_DOCKER_IMAGE)
        except docker.errors.ImageNotFound:
            print(f'{WEB_API_DOCKER_IMAGE} not found locally')
            print(f"Pulling web-api image {WEB_API_DOCKER_IMAGE}....")
            docker_image_pull_with_progress(client, WEB_API_DOCKER_IMAGE)

        # Start web api
        if web_api_running is False:
            print(f'Starting web service API at port {WEB_API_PORT}')
            if sys.platform == 'win32':
                DOCKER_SOCK = '//var/run/docker.sock'
            else:
                DOCKER_SOCK = '/var/run/docker.sock'

            client = docker.from_env()
            client.containers.run(
                WEB_API_DOCKER_IMAGE,
                ports={3002:WEB_API_PORT},
                detach=True,
                name=WEB_API_CONTAINER_NAME,
                volumes=[
                    f'{WEB_API_MODELS_REPO}:/models',
                    f'{WEB_API_CONFIG_FOLDER}:/config',
                    f'{DOCKER_SOCK}:/var/run/docker.sock'],  # Docker in docker
                command='python server.py --models-repo /models --config /config'
                )
            print(f'API endpoint available at: http://localhost:{WEB_API_PORT}')

        # Start web app
        if web_app_running is False:
            print(f'Starting web app at port {WEB_APP_PORT}')
            client = docker.from_env()
            client.containers.run(
                WEB_APP_DOCKER_IMAGE,
                ports={80:WEB_APP_PORT},
                detach=True,
                name=WEB_APP_CONTAINER_NAME)
            print(f'Webapp available at: http://localhost:{WEB_APP_PORT}')

    except docker.errors.NotFound as e:
        print(e)
        message = typer.style(e, fg=typer.colors.WHITE, bg=typer.colors.RED)
        typer.echo(message)
    except docker.errors.ContainerError as e:
        message = typer.style(e, fg=typer.colors.WHITE, bg=typer.colors.RED)
        typer.echo(message)
    except docker.errors.APIError as e:
        message = typer.style(e, fg=typer.colors.WHITE, bg=typer.colors.RED)
        typer.echo(message)


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
        web_service_container.remove()

        print(f'Stop API service....')
        web_api_container = client.containers.get(WEB_API_CONTAINER_NAME)
        web_api_container.stop()
        web_api_container.remove()

        print(f'Done.')
    except docker.errors.NotFound :
        message = typer.style(f"Web-server not running", fg=typer.colors.WHITE, bg=typer.colors.RED)
        typer.echo(message)

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