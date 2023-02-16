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
from config import TRITON_HTTP_URL

from events.events_engine import EventsEngine
from enum import Enum

class Event(str, Enum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'

class SmokeAndFireDetection(Scenario):
    def __init__(self, scenario_name, camera_name=0, events=None, triton_url=TRITON_HTTP_URL):

        from models.triton_client_yolov5 import yolov5_triton
        self.model = yolov5_triton(triton_url, scenario_name)
        self.f_event =  EventsEngine(use_redis=True)
        super().__init__(scenario_name, camera_name, events, triton_url)


    def start(self, camera_name=0):
        '''
        Stream processing

        When running a scenario - the caller can specify any specific camera.
        '''

        import cv2
        stream = camera_name

        print(f'Opening capture for {stream}')
        video = cv2.VideoCapture(stream)
        fire_count = 0
        while True:
            # Do processing
            ret, frame = video.read()
            if ret is False:
                LOGGER.error('ERROR: reading from video frame')
                time.sleep(1)
                continue

            # Detect smoke & fire
            results = self.model(frame, size=640)  # batched inference

            det = results.xyxy[0]

            if len(det):
                for *xyxy, conf, cls in reversed(det):
                    if int(cls.item()) == 0:
                        fire_count += 1

            if fire_count > 5:
                self.f_event.fire_event(Event.CRITICAL, 'WEBCAM', "smoke-and-fire-detection", 'FIRE_DETECTED', {})


            results.print()
            results.show()
            # if results contains smoke or fire class --> then fire an event here.
            # For now fire-an-event == print the event details.

            # if stop_evt is set, then break
            if self.stop_evt.is_set():
                break

def camera_stream():
    snf = SmokeAndFireDetection(scenario_name = 'smoke-and-fire-detection')
    snf.start(camera_name=0)

if __name__ == '__main__':
    camera_stream()