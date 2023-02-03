import cv2
from rich import print
import time

import sys
from pathlib import Path
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # visionai/visionai directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

from util.general import LOGGER
from scenarios import Scenario
from models.triton_client_yolov5 import yolov5_triton

class SmokeAndFireDetection(Scenario):
    def __init__(self, scenario_name, camera=None, events=None, triton_url='localhost:8000'):
        self.model = yolov5_triton(triton_url, scenario_name)
        super().__init__(scenario_name, camera, events, triton_url)


    def start(self, stream=None):
        '''
        Stream processing
        '''
        print(f'Opening capture for {stream}')
        video = cv2.VideoCapture(stream)

        while True:
            # Do processing
            ret, frame = video.read()
            if ret is False:
                LOGGER.error('ERROR: reading from video frame')
                time.sleep(1)
                continue

            # Detect smoke & fire
            results = self.model(frame, size=640)  # batched inference
            results.print()
            results.save()

            # if stop_evt is set, then break
            if self.stop_evt.is_set():
                break

