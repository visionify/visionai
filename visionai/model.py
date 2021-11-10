import cv2
import os
import requests
import glob

from .exceptions import *
from .constants import Config, Engine


class Model():
    def _check_local(self, model_name: str):
        return os.path.exists(os.path.join(Config.models_dir, model_name))

    # TODO: Maybe support this later. Automatically download appropriate models
    # Or maybe implement it as visionai CLI to download any models.
    # def _check_cloud(self, model_name: str):
    #     return True

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
        if self._check_local(model_name) is False:
            raise VisionAiValueError('Model: {} not found'.format(model_name))

        self._model_name = model_name
        self._model_dir = self._get_model_dir(model_name)
        self._model_file = self._get_model_file(model_name)
        self._model_protofile = self._get_model_protofile(model_name)
        self._model_labels = self._get_model_labels(model_name)
        self._model_inp_w, self._model_inp_h = (300, 300) # TODO: Do it correctly for all platforms.
        self._net = None

    def _get_model_dir(self, model_name: str):
        return os.path.join(Config.models_dir, model_name)

    def _get_model_file(self, model_name: str):
        # TODO: Do this correctly later.
        model_files = glob.glob(os.path.join(self._get_model_dir(model_name), '*.caffemodel'))
        if model_files is not None and len(model_files) > 0:
            return model_files[0]
        else:
            raise VisionAiValueError('Model: {} not found'.format(model_name))

    def _get_model_protofile(self, model_name: str):
        # TODO: Do this correctly later.
        model_protofiles = glob.glob(os.path.join(self._get_model_dir(model_name), '*_prototxt.txt'))
        if model_protofiles is not None and len(model_protofiles) > 0:
            return model_protofiles[0]
        else:
            raise VisionAiValueError('Model Protofile: {} not found'.format(model_name))

    def _get_model_labels(self, model_name: str):
        # TODO: Do this correctly later.
        model_labels = glob.glob(os.path.join(self._get_model_dir(model_name), 'labels.txt'))
        if model_labels is not None and len(model_labels) > 0:
            return model_labels[0]
        else:
            raise VisionAiValueError('Model Labels: {} not found'.format(model_name))

    def load_model(self):
        # Load caffemodel on Linux(x86)/Mac platform
        if 'caffemodel' in self._model_file:
            self._net = cv2.dnn.readNetFromCaffe(self._model_protofile, self._model_file)

    def detect(self, frame):
        if 'caffemodel' in self._model_file:
            blob = cv2.dnn.blobFromImage(
                cv2.resize(frame, (300, 300)),
                scalefactor=0.007843,
                size=(300, 300),
                mean=127.5
            )
            self._net.setInput(blob)
            detections = self._net.forward()
            return detections






