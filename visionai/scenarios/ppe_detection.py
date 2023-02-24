from rich import print
import time

import sys
from pathlib import Path
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # visionai/visionai directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
from models.plots import Annotator
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

class PpeDetection(Scenario):
    def __init__(self, scenario_name, camera_name=0, events=None, triton_url=TRITON_HTTP_URL):
        self.f_event =  EventsEngine(use_redis=True)
        from models.triton_client_yolov5 import yolov5_triton
        labels_file = ROOT / 'models-repo' / 'ppe-detection' / 'labels.txt'
        with open(labels_file, 'r') as f:
            labels = [line.strip() for line in f.readlines()]
        self.model = yolov5_triton(triton_url, scenario_name)
        self.model.conf = 0.35
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

        while True:
            # Do processing
            ret, image = video.read()
            if ret is False:
                LOGGER.error('ERROR: reading from video frame')
                time.sleep(1)
                continue
            
            # Load model
            pay_load = {'safety-goggles' : 'No',
                        'gloves' : 'No',
                        'safety-helmet' : 'No',
                        'safety-mask' : 'No',
                        'safety-shoes' : 'No',
                        'person' : 'No',
                        'safety-vest' : 'No',
                        'safety-harness' : 'No',
                        'head' : 'No',
                        'no-gloves' : 'No',
                        'no-safety-shoes' : 'No',
                        'no-mask' : 'No'
                        }
            results = self.model(image, size=640) #, visualize=False)
            stride, names= self.model.stride, self.model.names
            im0 = image
            
            det = results.xyxy[0]
            # seen += 1
            annotator = Annotator(im0, line_width=3) #, example=str(names))
            
            if len(det):
                for *xyxy, conf, cls in reversed(det):
                    c = int(cls)  # integer class
                    label = f'{names[c]} {conf:.2f}'
                    print(label)
                    if 'class0' in label:
                        pay_load['safety-goggles'] = 'Yes'
                        annotator.box_label(xyxy, 'safety-goggles')
                    elif 'class1' in label:
                        pay_load['gloves'] = 'Yes'
                        annotator.box_label(xyxy, 'gloves')
                    elif 'class2' in label:
                        pay_load['safety-helmet'] = 'Yes'
                        annotator.box_label(xyxy, 'safety-helmet')
                    elif 'class3' in label:
                        pay_load['safety-mask'] = 'Yes'
                        annotator.box_label(xyxy, 'safety-mask')
                    elif 'class4' in label:
                        pay_load['safety-shoes'] = 'Yes'
                        annotator.box_label(xyxy, 'safety-shoes')
                    elif 'class6' in label:
                        pay_load['safety-vest'] = 'Yes'
                        annotator.box_label(xyxy, 'safety-vest')
                    elif 'class7' in label:
                        pay_load['safety-harness'] = 'Yes'
                        annotator.box_label(xyxy, 'safety-harness')
                    elif 'class8' in label:
                        pay_load['head'] = 'Yes'
                        annotator.box_label(xyxy, 'head')
                    elif 'class9' in label:
                        pay_load['no-gloves'] = 'Yes'
                        annotator.box_label(xyxy, 'no-gloves')
                    elif 'class10' in label:
                        pay_load['no-safety-shoes'] = 'Yes'
                        annotator.box_label(xyxy, 'no-safety-shoes')
                    elif 'class11' in label:
                        pay_load['no-mask'] = 'Yes'
                        annotator.box_label(xyxy, 'no-mask')
                    # annotator.box_label(xyxy, label)
                    self.f_event.fire_event(Event.INFO, 'OFFICE-01', 'ppe-detection', 'PPE_Detection', pay_load)
                im0 = annotator.result()
            if self.stop_evt.is_set():
                    break
            cv2.imshow('detection', im0)
            if cv2.waitKey(5) & 0xFF == 27:
                break
        video.release()
        cv2.destroyAllWindows()

def camera_stream():
    snf = PpeDetection(scenario_name = 'ppe-detection')
    snf.start(camera_name=0)

if __name__ == '__main__':
    # people_taking_picture_detection()
    camera_stream()