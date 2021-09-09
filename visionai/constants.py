import enum
import os

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


