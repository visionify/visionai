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

class FaceBlur(Scenario):
    def __init__(self, scenario_name='face-blur', camera_name=0, events=None, triton_url=TRITON_HTTP_URL):

        from models.triton_client_yolov5 import yolov5_triton
        self.model = yolov5_triton(triton_url, 'yolov5s-face')
        super().__init__(scenario_name, camera_name, events, triton_url)

    # API that face_blur module exports. Use it like this:
    # from scenario.face_blur import FaceBlur
    # fb = FaceBlur()
    # out_img = fb.blur_faces(img)  # provide cv2 image.
    def blur_faces(self, img):
        import cv2
        results = self.model(img, size=640)



    def start(self, camera_name=0):
        '''
        Stream processing

        When running a scenario - the caller can specify any specific camera.
        '''

        import cv2
        stream = camera_name

        print(f'Opening capture for {stream}')
        video = cv2.VideoCapture(stream)

        while True:
            # Do processing
            ret, frame = video.read()
            if ret is False:
                LOGGER.error('ERROR: reading from video frame')
                time.sleep(1)
                continue

            # Detect Faces
            results = self.model(frame, size=640)  # batched inference
            for box in results.xyxy[0]:
                xB = int(box[2])
                xA = int(box[0])
                yB = int(box[3])
                yA = int(box[1])
                cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 0, 0), -1)

            results.show()
            
            # if result contains people but PPE are not detected - then fire an event.
            # For now fire-an-event == print the event details.

            # if stop_evt is set, then break
            if self.stop_evt.is_set():
                break



