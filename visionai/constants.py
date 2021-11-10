import enum
import os

def get_platform():
    if os.name == 'nt':
        return 'windows'
    else:
        res = os.uname()
        os_name = res.sysname
        os_release = res.release
        os_version = res.version
        if 'tegra' in os_release:
            return 'jetson'
        elif 'Darwin' in os_version:
            return 'macos'
        elif 'Linux' in os_name:
            return 'linux'


class Engine(enum.Enum):
    """
    Different DNN Engines that can be supported.
    DNN - OpenCV DNN Backend.
    CUDA - CUDA DNN Backend. (AMD platform + NVIDIA Graphics Card)
    TENSOR_RT - TensorRT DNN Backend. (Jetson platform)
    """
    DNN = 'DNN'
    CUDA = 'CUDA'
    TENSOR_RT = 'TENSOR_RT'


class Config:
    home_dir = os.path.join(os.path.expanduser('~'), '.visionai')
    models_dir = os.path.join(home_dir, 'models')

    #TODO: This needs to be done during pip install visionai
    #os.makedirs(home_dir, exist_ok=True)
    #os.makedirs(models_dir, exist_ok=True)

    api_server = 'http://localhost:8010'

    # Right now only supporting jetson (Nano/Xavier NX) & Intel based Windows/Linux/Mac.
    # platform can have values: windows, macos, linux, jetson
    platform = get_platform()
