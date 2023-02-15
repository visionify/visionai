import docker
from rich import print
from rich.progress import Progress
from config import GRAFANA_ENABLED, GRAFANA_SERVER_DOCKER_IMAGE, GRAFANA_SERVER_PORT, GRAFANA_CONTAINER_NAME, GRAFANA_DATA_DIR, GRAFANA_PROVISIONING_DIR
from config import REDIS_ENABLED, REDIS_SERVER_DOCKER_IMAGE, REDIS_SERVER_PORT, REDIS_CONTAINER_NAME, DOCKER_NETWORK
from util.general import check_requirements

tasks = {}

def docker_image_pull_with_progress(client, image_name):

    # Show task progress (red for download, green for extract)
    def show_progress(line, progress):
        if line['status'] == 'Downloading':
            id = f'[red][Download {line["id"]}]'
        elif line['status'] == 'Extracting':
            id = f'[green][Extract  {line["id"]}]'
        else:
            print(line)
            # skip other statuses
            return

        if id not in tasks.keys():
            tasks[id] = progress.add_task(f"{id}", total=line['progressDetail']['total'])
        else:
            progress.update(tasks[id], completed=line['progressDetail']['current'])


    print(f'Pulling image: {image_name}')
    with Progress() as progress:
        resp = client.api.pull(image_name, stream=True, decode=True)
        for line in resp:
            show_progress(line, progress)

def docker_container_run_triton(
    client:docker.DockerClient,     # docker.from_env()
    image,                          # image name
    container_name,                 # container name
    command,                        # command to run in container
    stdout=False,                   # disable logs
    stderr=False,                   # disable stderr logs
    detach=True,                    # detached mode - daemon
    remove=True,                    # remove fs after exit
    auto_remove=True,               # remove fs if container fails
    device_requests=None,           # pass GPU
    network_mode='host',            # --net=host
    volumes=[],                     # -v ./models-repo:/models
    ports={}                        # -p 8000:8000 etc (needed for mac)
):
    ctainer = None
    container_type = 'MODEL_SERVER'
    try:
        print('Try model-server with NVIDIA runtime & GPUs.')
        ctainer = client.containers.run(
            image=image,
            name=container_name,
            command=command,
            stdout=stdout,
            stderr=stderr,
            detach=detach,
            remove=remove,
            auto_remove=auto_remove,
            runtime='nvidia',   # Use nvidia-container-runtime
            device_requests=device_requests,
            # network_mode=network_mode,
            volumes=volumes,
            ports=ports
        )
        container_type = 'NVIDIA Runtime + GPU'
    except Exception as ex:
        ctainer = None
        print('.... Failed.')

    if ctainer is None:
        print('Try model-server without NVIDIA runtime + CPUs')

        try:
            ctainer = client.containers.run(
                image=image,
                name=container_name,
                command=command,
                stdout=stdout,
                stderr=stderr,
                detach=detach,
                remove=remove,
                auto_remove=auto_remove,
                device_requests=device_requests,
                # network_mode=network_mode,
                volumes=volumes,
                ports=ports
            )
            container_type = 'NVIDIA Runtime + CPU'
        except Exception as ex:
            ctainer = None
            print('.... Failed.')

    if ctainer is None:
        print('Try model-server with default runtime + CPU')

        try:
            ctainer = client.containers.run(
                image=image,
                name=container_name,
                command=command,
                stdout=stdout,
                stderr=stderr,
                detach=detach,
                remove=remove,
                auto_remove=auto_remove,
                # network_mode=network_mode,
                volumes=volumes,
                ports=ports
            )
            container_type = 'Default Runtime + CPU'
        except Exception as ex:
            ctainer = None
            print('.... Failed.')

    if ctainer is None:
        print('ERROR: Giving up.')
        return None
    else:
        print('.... Success.')
        print(f'Started model server successfully: {container_type}')
        return ctainer

def docker_container_is_running(container_name):
    client = docker.from_env()
    containers = client.containers.list(all=True)
    for container in containers:
        if container.name == container_name:
            return container.status == 'running'
    return False

def docker_network_is_running(network_name):
    client = docker.from_env()
    networks = client.networks.list()
    for network in networks:
        if network.name == network_name:
            return True
    return False

def docker_network_start(network_name):
    client = docker.from_env()
    if docker_network_is_running(network_name=network_name):
        print(f'{network_name} network already running.')
        return
    print(f'Starting {network_name} network...')
    client.networks.create(network_name, driver='bridge')

def docker_network_join(network_name, container_name):
    client = docker.from_env()
    network = client.networks.get(network_name)
    container = client.containers.get(container_name)
    network.connect(container)

def docker_container_start(
    container_name:str,
    image:str,
    portmap:dict=None,
    envmap:dict=None,
    network_name:str=None,
    volmap:dict=[],
    command:str=None):
    '''
    Start a docker container.

    Args:
        container_name (str): Name of container
        image (str): Name of image
        portmap (dict): Port mapping. Example: {8000:8000, 8001:8001, 8002:8002}
        envmap (dict): Environment variables. Example: {'GF_AUTH_ANONYMOUS_ORG_ROLE': 'Admin'}
        volmap (list): Volume mapping. Example: ['./models-repo:/models']
        network_name (str): Name of network to create + join
        command (str): Command to run in container
    '''
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

    # If container already running, do nothing
    if docker_container_is_running(container_name=container_name):
        print(f'{container_name} container already running.')
        return

    # Pull image
    print(f'Pulling {image} image...')
    client = docker.from_env()
    docker_image_pull_with_progress(client=client, image_name=image)

    # Ports mapping
    if portmap is not None:
        ports = []
        for k in portmap.keys():
            ports.append(f'-p {k}:{portmap[k]}')
        ports = ' '.join(ports)
    else:
        ports = ''

    # Environment variables
    if envmap is not None:
        envs = []
        for k in envmap.keys():
            envs.append(f'-e {k}={envmap[k]}')
        envs = ' '.join(envs)
    else:
        envs = ''

    # Volume mapping
    if volmap is not None:
        volumes = []
        for k in volmap:
            volumes.append(f'-v {k}')
        volumes = ' '.join(volumes)
    else:
        volumes = ''

    # Network name
    if network_name is not None:
        print(f'Joining network...{network_name}')
        docker_network_start(network_name=network_name)

    # Command to run
    if command is None:
        command = ''

    # Run container
    print(f'Running {image} container...')

    cmd_line = f'docker run -d --rm --name {container_name} {ports} {envs} {volumes} {image} {command}'
    cmd_line_hint = False
    try:
        container = client.containers.run(
            image=image,
            name=container_name,
            detach=True,
            remove=True,
            auto_remove=True,
            ports=portmap,
            environment=envmap,
            volumes=volmap,
            network=network_name,
            command=command
        )
    except docker.errors.APIError as e:
        print(f'Error: {e}')
        print(f'{image} container already running. Skipping.')
        cmd_line_hint = False
    except docker.errors.ImageNotFound as e:
        print(f'Error: {e}')
        print(f'{image} image not found. Skipping.')
        cmd_line_hint = True
    except docker.errors.ContainerError as e:
        print(f'Error: {e}')
        print(f'{image} container error. Skipping.')
        cmd_line_hint = True
    except docker.errors.DockerException as e:
        print(f'Error: {e}')
        print(f'{image} docker error. Skipping.')
        cmd_line_hint = True
    except Exception as e:
        print(f'Error: {e}')
        print(f'{image} error. Skipping.')
        cmd_line_hint = True

    # Print command line hint
    if cmd_line_hint:
        print('You can run the following command line to start the {image} container:')
        print(cmd_line)
    else:
        pass

        #     docker_network_join(network_name=network_name, container_name=container_name)

    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')


def docker_container_stop(container_name):
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

    # Stop container
    print(f'Stopping {container_name} container...')
    cmd_hint = False
    cmd_line = f'docker stop {container_name}'

    client = docker.from_env()
    try:
        container = client.containers.get(container_name)
        container.stop()
    except docker.errors.NotFound as e:
        print(f'{container_name} container not found. Skipping.')
        cmd_hint = True
    except docker.errors.APIError as e:
        print(f'Error: {e}')
        print(f'{container_name} container API error. Skipping.')
        cmd_hint = True
    except docker.errors.DockerException as e:
        print(f'Error: {e}')
        print(f'{container_name} docker error. Skipping.')
        cmd_hint = True
    except Exception as e:
        print(f'Error: {e}')
        print(f'{container_name} error. Skipping.')
        cmd_hint = True

    # Print command line hint
    if cmd_hint:
        print(f'You can run the following command line to stop the {container_name} container:')
        print(cmd_line)

    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')


def redis_container_start():
    # If redis is not enabled, do nothing
    if REDIS_ENABLED == False:
        print('Redis is not enabled. Skipping installation.')
        return

    # Start redis container
    docker_container_start(
        container_name=REDIS_CONTAINER_NAME,
        image=REDIS_SERVER_DOCKER_IMAGE,
        network_name=DOCKER_NETWORK,
        portmap={6379:REDIS_SERVER_PORT}
        )

def redis_container_stop():
    # If redis is not enabled, do nothing
    if REDIS_ENABLED == False:
        print('Redis is not enabled. Skip redis container stop.')

    # Stop redis container
    docker_container_stop(container_name=REDIS_CONTAINER_NAME)

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


def grafana_container_start():
    # If grafana is not enabled, do nothing
    if GRAFANA_ENABLED == False:
        print('Grafana is not enabled. Skipping installation.')
        return

    # Grafana default env parameters
    grafana_env = {
        'GF_AUTH_ANONYMOUS_ORG_ROLE': 'Admin',
        'GF_AUTH_ANONYMOUS_ENABLED': True,
        'GF_AUTH_BASIC_ENABLED': False,
        'GF_ENABLE_GZIP': True,
        'GF_USERS_DEFAULT_THEME': 'dark',
        'GF_DEFAULT_APP_MODE': 'development',
        'GF_INSTALL_PLUGINS': 'redis-datasource'
    }

    # Start grafana container
    docker_container_start(
        container_name=GRAFANA_CONTAINER_NAME,
        image=GRAFANA_SERVER_DOCKER_IMAGE,
        network_name=DOCKER_NETWORK,
        portmap={3000:GRAFANA_SERVER_PORT},
        envmap=grafana_env,
        volmap=[f'{GRAFANA_DATA_DIR}:/var/lib/grafana', f'{GRAFANA_PROVISIONING_DIR}:/etc/grafana/provisioning/datasources']
        )

def grafana_container_stop():
    # If grafana is not enabled, do nothing
    if GRAFANA_ENABLED == False:
        print('Grafana is not enabled. Skip grafana container stop.')

    # Stop grafana container
    docker_container_stop(container_name=GRAFANA_CONTAINER_NAME)


if __name__ == '__main__':
    # Pull a large image
    # client = docker.from_env()
    # IMAGE_NAME = 'bitnami/pytorch'
    # docker_image_pull_with_progress(client, IMAGE_NAME)

    # check if container is running
    redis_is_running = docker_container_is_running('redis')
    print(f'redis_is_running: {redis_is_running}')
