import os
import sys
import docker

from pathlib import Path
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # Root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

from config import REDIS_ENABLED, REDIS_SERVER_DOCKER_IMAGE, REDIS_SERVER_PORT, REDIS_CONTAINER_NAME
from util.docker_utils import docker_image_pull_with_progress, docker_conatiner_is_running
from util.general import check_requirements
from rich import print

def redis_container_start():
    # If redis is not enabled, do nothing
    if REDIS_ENABLED == False:
        print('Redis is not enabled. Skipping installation.')
        return

    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

    # If container already running, do nothing
    if docker_conatiner_is_running(container_name=REDIS_CONTAINER_NAME):
        print('Redis container already running. Skipping installation.')
        return

    # Pull redis image
    print('REDIS Installation')
    print('Pulling redis image...')
    client = docker.from_env()
    docker_image_pull_with_progress(client=client, image_name=REDIS_SERVER_DOCKER_IMAGE)

    # Run redis container
    print('Running redis container...')
    cmd_line = f'docker run -d --rm --name redis -p {REDIS_SERVER_PORT}:{REDIS_SERVER_PORT} {REDIS_SERVER_DOCKER_IMAGE}'
    cmd_line_hint = False
    try:
        container = client.containers.run(
            image=REDIS_SERVER_DOCKER_IMAGE,
            name=REDIS_CONTAINER_NAME,
            detach=True,
            remove=True,
            auto_remove=True,
            ports={REDIS_SERVER_PORT: REDIS_SERVER_PORT}
        )
    except docker.errors.APIError as e:
        print(f'Error: {e}')
        print('Redis container already running. Skipping.')
        cmd_line_hint = False
        return
    except docker.errors.ImageNotFound as e:
        print(f'Error: {e}')
        print('Redis image not found. Skipping.')
        cmd_line_hint = True
        return
    except docker.errors.ContainerError as e:
        print(f'Error: {e}')
        print('Redis container error. Skipping.')
        cmd_line_hint = True
        return
    except docker.errors.DockerException as e:
        print(f'Error: {e}')
        print('Redis docker error. Skipping.')
        cmd_line_hint = True
        return
    except Exception as e:
        print(f'Error: {e}')
        print('Redis error. Skipping.')
        cmd_line_hint = True
        return

    # Print command line hint
    if cmd_line_hint:
        print('You can run the following command line to start the redis container:')
        print(cmd_line)

    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')


def redis_container_stop():
    # If redis is not enabled, do nothing
    if REDIS_ENABLED == False:
        print('Redis is not enabled. Skip redis container stop.')

    # Stop redis container
    print('Stopping redis container...')
    cmd_hint = False
    cmd_line = f'docker stop {REDIS_CONTAINER_NAME}'

    client = docker.from_env()
    try:
        container = client.containers.get(REDIS_CONTAINER_NAME)
        container.stop()
    except docker.errors.NotFound as e:
        print(f'Error: {e}')
        print('Redis container not found. Skipping.')
        cmd_hint = True
        return
    except docker.errors.APIError as e:
        print(f'Error: {e}')
        print('Redis container API error. Skipping.')
        cmd_hint = True
        return
    except docker.errors.DockerException as e:
        print(f'Error: {e}')
        print('Redis docker error. Skipping.')
        cmd_hint = True
        return
    except Exception as e:
        print(f'Error: {e}')
        print('Redis error. Skipping.')
        cmd_hint = True
        return

    # Print command line hint
    if cmd_hint:
        print('You can run the following command line to stop the redis container:')
        print(cmd_line)

def redis_python_install():
    # If redis is not enabled, do nothing
    if REDIS_ENABLED == False:
        print('Redis is not enabled. Skipping installation.')
        return

    # Install redis python package
    print('Installing redis python package...')
    cmd_hint = False
    cmd_line = f'pip install redis'

    try:
        check_requirements(['redis'], install=True)
    except Exception as e:
        print(f'Error: {e}')
        print('Redis python package installation failed. Skipping.')
        cmd_hint = True
        return

    # Print command line hint
    if cmd_hint:
        print('You can run the following command line to install the redis python package:')
        print(cmd_line)


def redis_python_package_installed():
    return 'redis' not in check_requirements('redis', install=False)

if __name__ == '__main__':
    redis_container_start()
