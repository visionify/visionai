import docker
from rich.progress import Progress

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

def docker_container_run(
    client:docker.DockerClient,     # docker.from_env()
    image,                          # image name
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

def docker_conatiner_is_running(container_name):
    client = docker.from_env()
    containers = client.containers.list(all=True)
    for container in containers:
        if container.name == container_name:
            return container.status == 'running'
    return False


if __name__ == '__main__':
    # Pull a large image
    # client = docker.from_env()
    # IMAGE_NAME = 'bitnami/pytorch'
    # docker_image_pull_with_progress(client, IMAGE_NAME)

    # check if container is running
    redis_is_running = docker_conatiner_is_running('redis')
    print(f'redis_is_running: {redis_is_running}')
