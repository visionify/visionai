import docker
from rich import print
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
import time
from urllib.parse import urlparse

import sys
from pathlib import Path
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # visionai/visionai directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

from config import TRITON_HTTP_URL, TRITON_SERVER_DOCKER_IMAGE, TRITON_SERVER_EXEC, TRITON_SERVER_COMMAND, TRITON_MODELS_REPO, TRITON_SERVER_CONTAINER_NAME

class TritonClient():

    # Models start command
    MODELS_SERVE_CMD = '[magenta]visionai models serve[/magenta]'
    MODELS_AVAIL_CMD = '[magenta]visionai models check[/magenta]'
    MODELS_DOWNLOAD_CMD = '[magenta]visionai models download[/magenta]'
    MODELS_STOP_CMD = '[magenta]visionai models stop[/magenta]'
    MODELS_RESTART_CMD = '[magenta]visionai models resatart[/magenta]'
    MODELS_STATUS_CMD = '[magenta]visionai models status[/magenta]'

    def __init__(self) -> None:

        # create client.
        self.docker_client = docker.from_env()

        # console tty
        self.console = Console()

        # Initialize trition client
        self.triton_client = None
        self.init_triton_client()


    def init_triton_client(self):
        # Triton client
        try:
            import tritonclient.http
            parsed_url = urlparse(TRITON_HTTP_URL)
            self.triton_client = tritonclient.http.InferenceServerClient(url=parsed_url.netloc)
            self.triton_client.get_server_metadata()
        except Exception as ex:
            self.triton_client = None

    # Print primitives
    def _get_pretty_container(self, ctainer, image_name=None):
        if ctainer is None:
            return f'None\n[yellow]{image_name}[/yellow]\n[b][red]Not running[/red][/b]'

        id = f'{ctainer.attrs["Id"][:10]}'  # can refer to ctainer by first 10 digits
        name = f'{ctainer.attrs["Name"]}'
        image = f'{ctainer.attrs["Config"]["Image"]}'
        command = ctainer.attrs["Path"] + " " +  " ".join(ctainer.attrs["Args"])
        entrypoint = ctainer.attrs['Config']['Entrypoint']
        command2 = " ".join(ctainer.attrs['Config']['Cmd'])
        status_str = ctainer.attrs['State']['Status']  # "Running" or "Dead" or "Paused"
        status = ctainer.attrs['State']['Running'] # True/False
        started_at = ctainer.attrs['State']['StartedAt'] # 2023-01-29T17:01:13.428140501Z (isoformat string)
        finished_at = ctainer.attrs['State']['FinishedAt'] # 2023-01-29T17:01:13.428140501Z (isoformat string)
        ports = ctainer.attrs['NetworkSettings']['Ports'] # {}
        if status:
            status_str = f'[green][b]{status_str}[/b][/green] since {started_at[:19]}'
        else:
            status_str = f'[red][b]{status_str}[/b][/red] since {finished_at[:19]}'
        ctainer_pretty = f'{id}: [magenta]{name}[/magenta]\n[yellow]{image}[/yellow]\n[blue]{command}[/blue]\n{status_str}'
        return ctainer_pretty

    def _get_pretty_containers(self):
        containers = []
        for ctainer in self.docker_client.containers.list():
            containers.append(Panel(self._get_pretty_container(ctainer), width=50))
        return containers

    def print_pretty_container(self, container, image_name=None):
        '''
        Print a container (with optional image name)
        '''
        if image_name is not None or container is None:
            title = image_name
        else:
            title = container.attrs["Config"]["Image"]

        title = f'Containers for image: [i][yellow]*{title}*[/yellow][/i]'
        self.console.print(Panel(self._get_pretty_container(container, image_name), title=title, expand=False))

    def print_pretty_containers(self):
        '''
        Prettify & print all running containers
        '''
        self.console.print(Panel(Columns(self._get_pretty_containers()), title="Running Containers", expand=False))


    def get_container_by_image_name(self, image_name):
        '''
        Get containers by an image name (incl. partial)
        '''
        for ctainer in self.docker_client.containers.list():
            if image_name.lower() in ctainer.attrs['Config']['Image']:
                return ctainer
        return None

    def is_triton_running(self):
        '''
        Check if triton server is running
        '''
        ctainer = self.get_container_by_image_name(TRITON_SERVER_EXEC)
        if ctainer is not None and self.triton_client is None:
            self.init_triton_client()

        return ctainer is not None

    def _get_pretty_models(self, models):
        ret = []
        for model in models:
            model_name = model['name']

            # Model config
            # Ex:
            # {
            #     'name': 'ppe-detection',
            #     'platform': 'onnxruntime_onnx',
            #     'backend': 'onnxruntime',
            #     'version_policy': {'latest': {'num_versions': 1}},
            #     'max_batch_size': 0,
            #     'input': [
            #         {
            #             'name': 'images',
            #             'data_type': 'TYPE_FP32',
            #             'format': 'FORMAT_NONE',
            #             'dims': [1, 3, 640, 640],
            #             'is_shape_tensor': False,
            #             'allow_ragged_batch': False,
            #             'optional': False
            #         }
            #     ],
            #     'output': [
            #         {
            #             'name': 'output0',
            #             'data_type': 'TYPE_FP32',
            #             'dims': [1, 25200, 14],
            #             'label_filename': 'labels.txt',
            #             'is_shape_tensor': False
            #         }
            #     ],
            #     'batch_input': [],
            #     'batch_output': [],
            #     'optimization': {
            #         'priority': 'PRIORITY_DEFAULT',
            #         'input_pinned_memory': {'enable': True},
            #         'output_pinned_memory': {'enable': True},
            #         'gather_kernel_buffer_threshold': 0,
            #         'eager_batching': False
            #     },
            #     'instance_group': [
            #         {
            #             'name': 'ppe-detection',
            #             'kind': 'KIND_GPU',
            #             'count': 1,
            #             'gpus': [0],
            #             'secondary_devices': [],
            #             'profile': [],
            #             'passive': False,
            #             'host_policy': ''
            #         }
            #     ],
            #     'default_model_filename': 'model.onnx',
            #     'cc_model_filenames': {},
            #     'metric_tags': {},
            #     'parameters': {},
            #     'model_warmup': []
            # }
            model_config = self.triton_client.get_model_config(model_name)
            platform = model_config['backend']  # onnxruntime
            model_input  = 'IN[0] :' + model_config['input'][0]['data_type'] + ' ' + str(model_config['input'][0]['dims'])
            model_output = 'OUT   :' + model_config['output'][0]['data_type'] + ' ' + str(model_config['output'][0]['dims'])

            # Inference stats
            # Ex:
            # {
            #     'model_stats': [
            #         {
            #             'name': 'ppe-detection',
            #             'version': '1',
            #             'last_inference': 0,
            #             'inference_count': 0,
            #             'execution_count': 0,
            #             'inference_stats': {
            #                 'success': {'count': 0, 'ns': 0},
            #                 'fail': {'count': 0, 'ns': 0},
            #                 'queue': {'count': 0, 'ns': 0},
            #                 'compute_input': {'count': 0, 'ns': 0},
            #                 'compute_infer': {'count': 0, 'ns': 0},
            #                 'compute_output': {'count': 0, 'ns': 0},
            #                 'cache_hit': {'count': 0, 'ns': 0},
            #                 'cache_miss': {'count': 0, 'ns': 0}
            #             },
            #             'batch_stats': []
            #         }
            #     ]
            # }
            inf_success = 'INF ✅:' + str(self.triton_client.get_inference_statistics(model_name)['model_stats'][0]['inference_stats']['success'])
            inf_fail    = 'INF ❌:' + str(self.triton_client.get_inference_statistics(model_name)['model_stats'][0]['inference_stats']['fail'])

            model_status = f"[green]{model['state']}[/green]" if model['state'].upper() == 'READY' else f"[red]{model['state']}[/red]"
            model_panel = f"[magenta]{model_name}[/magenta]\n" + \
                f"[blue]version {model['version']}[/blue] - {model_status}\n" + \
                f"[grey50]{model_input}[/grey50]\n" + \
                f"[grey50]{model_output}[/grey50]\n" + \
                f"[green]{inf_success}[/green]\n" + \
                f"[dark_red]{inf_fail}[/dark_red]\n"

            ret.append(Panel(model_panel, title=platform, width=40, expand=False))
        return ret

    def get_models(self):
        '''
        Get models served by Triton container.
        '''

        # get_repository_index() example Output:
        # [
        #     {'name': 'phone-detection', 'version': '1', 'state': 'READY'},
        #     {'name': 'ppe-detection', 'version': '1', 'state': 'READY'},
        #     {'name': 'rust-and-corrosion-detection', 'version': '1', 'state': 'READY'},
        #     {'name': 'smoke-and-fire-detection', 'version': '1', 'state': 'READY'},
        #     {'name': 'smoking-detection', 'version': '1', 'state': 'READY'}
        # ]
        if self.triton_client is None:
            return None
        else:
            return self.triton_client.get_model_repository_index()

    def print_models_served(self):
        '''
        Print models being served by triton server
        '''
        triton_up = self.is_triton_running()
        models = self.get_models()
        if triton_up is False:
            panel_content = Panel(f'[red]ERROR: Model server is not running[/red]\nStart model server with:\n{self.MODELS_SERVE_CMD}', title='Models running:')
        elif models is None or len(models) == 0:
            panel_content = Panel(f'[red]ERROR: No models found![/red]\nCheck model status with:\n{self.MODELS_AVAIL_CMD} \n{self.MODELS_DOWNLOAD_CMD}\n\nYou can also restart the model server with \n{self.MODELS_RESTART_CMD}', title='Models running:')
        else:
            panel_content = Panel(Columns(self._get_pretty_models(models), title='Models running:'))

        self.console.print(panel_content)


    def start_model_server(self):
        '''
        Start the model server

        Implements `visionai models serve` command
        '''

        if self.get_container_by_image_name(TRITON_SERVER_EXEC) is not None:
            print('Model server already running!')
            return

        try:
            print('Pulling docker image (this may take a while)')
            from util.docker_utils import docker_image_pull_with_progress, docker_container_run_triton

            # Stream progress message while pulling the docker image.
            docker_image_pull_with_progress(self.docker_client, image_name=TRITON_SERVER_DOCKER_IMAGE)
            print('Done.')

            # Try starting docker container with NVIDIA runtime,
            # If that is not available - then start the container with regular runtime
            print('Starting model server')
            docker_container_run_triton(
                client=self.docker_client,
                image=TRITON_SERVER_DOCKER_IMAGE,   # image name
                container_name=TRITON_SERVER_CONTAINER_NAME, # container name
                command=TRITON_SERVER_COMMAND,      # command to run in container
                stdout=False,                       # disable logs
                stderr=False,                       # disable stderr logs
                detach=True,                        # detached mode - daemon
                remove=True,                        # remove fs after exit
                auto_remove=True,                   # remove fs if container fails
                device_requests=[                   # similar to --gpus=all ??
                    docker.types.DeviceRequest(capabilities=[['gpu']])
                    ],
                # network_mode='host',                # --net=host
                volumes=                            # -v
                    [f'{TRITON_MODELS_REPO}:/models'],
                ports={
                    '8000': 8000,
                    '8001': 8001,
                    '8002': 8002
                }
            )

            init_complete = False
            init_idx = 0
            for init_idx in range(1,11):
                # sleep a bit
                time.sleep(1)

                # Attach triton_client
                self.init_triton_client()
                if self.triton_client is None:

                    # Check if container still present:
                    triton_container = self.get_container_by_image_name(TRITON_SERVER_EXEC)
                    if triton_container is None:
                        print('Container start failed.')
                        break

                    else:
                        print(f'[{init_idx}/{10}] Triton client init.')
                        continue

                else:
                    init_complete = True
                    break

            if init_complete is True:
                # Everything looks good
                print('Triton client initialized.')
                return True
            else:
                print('[red]- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -[/red]')
                print('[red]Error with starting triton container. (Likely one of the models is corrupt)[/red]')
                print()
                print('[magenta]Ensure the following command is successful:[/magenta]')
                models_repo_path = ROOT / 'models-repo'
                print(f'[magenta]docker run -it -p 8000:8000 -p 8001:8001 -p 8002:8002 -v {models_repo_path}:/models nvcr.io/nvidia/tritonserver:22.12-py3 tritonserver --model-repo /models[/magenta]')
                print('[red]- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -[/red]')
                return False

        except Exception as ex:
            print('ERROR: Trying to start model server.')
            print(f'Exception: {ex}')
            return False

    def stop_model_server(self):
        triton_container = self.get_container_by_image_name(TRITON_SERVER_EXEC)
        if triton_container is None:
            print('ERROR: Model server is not running')

        else:
            try:
                print('Stopping Model Server..')
                triton_container.stop()
                self.triton_client = None
                print('Done.')
            except Exception as ex:
                print(f'ERROR: Unable to stop model-server: {ex}')


if __name__ == '__main__':
    tc = TritonClient()
    # Print all running containers
    tc.print_pretty_containers()

    # Print a single container
    ctainer = tc.get_container_by_image_name(TRITON_SERVER_EXEC)
    tc.print_pretty_container(ctainer, TRITON_SERVER_EXEC)

    # Is triton running?
    triton_check = tc.is_triton_running()
    # print(f'Triton server status: {triton_check}')

    # Models served
    models = tc.get_models()
    # print(f'Models: {models}')

    # Print models
    tc.print_models_served()


    # Start model server
    tc.start_model_server()

    # Print models served
    tc.print_models_served()

    # Stop the model server
    tc.stop_model_server()
    tc.print_models_served()

    # Start the model server again
    tc.start_model_server()
    tc.print_models_served()

