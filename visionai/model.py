import os
import requests

from .exceptions import *
from .constants import Config, Engine


class Model():
    def _check_local(self, model_name: str):
        return os.path.exists(os.path.join(Config.models_dir, model_name))

    def _check_cloud(self, model_name: str):

        return

    def __init__(self, model_name: str):
        """
        Create a inference object based on model.

        :details
        Use a model based on its ID. If the model is not present locally,
        it is automatically downloaded to the device and loaded.

        :param model_name: A string like visionai/SSD-mobile-net-v2 that identifies the model.
        Based on your platform, correct model (Tensorflow or Caffe or TensorRT) will be
        downloaded to your device.
        This can also be a user-generated model. Example: test_user/SSD-mobile-net-v2-people
        This will download the user's specific model.
        """
        if self._check_local(model_name) is False and self._check_cloud(model_name) is False:
            raise VisionAiValueError('Model: {} not found'.format(model_name))
