from .bounding_box import BoundingBox
from .exceptions import *


class ObjectDetectionPrediction():
    """Object detection prediction class"""

    def __init__(self, box: BoundingBox, confidence: float, label, index=0):
        self._box = box
        self._confidence = confidence
        self._label = label
        self._index = index

    @property
    def box(self):
        return self._box

    @property
    def confidence(self):
        return self._confidence

    @property
    def label(self) -> str:
        return self._label

    @property
    def index(self):
        return self._index


class ObjectDetectionResults():
    """Results of object detection from ObjectDetection
    
    predictions is list of results sorted by descending values of confidence
    """

    def __init__(self, predictions: list, duration=0, image=None):
        if not isinstance(predictions, list):
            raise VisionAiInvalidFormat('predictions should be a list')

        self._predictions = predictions
        self._duration = duration
        self._image = image

    @property
    def predictions(self):
        return self._predictions

    @property
    def duration(self):
        return self._duration

    @property
    def image(self):
        return self._image


class ObjectDetection(Model):
    pass