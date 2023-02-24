from rich import print
import time

import sys
import cv2
import time

from pathlib import Path
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # visionai/visionai directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

from util.general import LOGGER
from scenarios import Scenario
from config import TRITON_HTTP_URL
from util.track import *

from events.events_engine import EventsEngine
from enum import Enum

class Event(str, Enum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'

class OccupancyMonitoring(Scenario):
    alert_time = 10
    def __init__(self, scenario_name, camera_name=0, events=None, triton_url=TRITON_HTTP_URL):

        from models.triton_client_yolov5 import yolov5_triton
        self.model = yolov5_triton(triton_url, scenario_name)
        self.f_event =  EventsEngine(use_redis=False)
        self.line_thickness=3
        super().__init__(scenario_name, camera_name, events, triton_url)


    def draw_boxes(self, img, bbox, count, total_time, offset=(0, 0)):
        for i, box in enumerate(bbox):
            x1, y1, x2, y2 = [int(i) for i in box]
            x1 += offset[0]
            x2 += offset[0]
            y1 += offset[1]
            y2 += offset[1]
            data = (int((box[0]+box[2])/2),(int((box[1]+box[3])/2)))
            label = f"ID: {str(count)} - Duration: {str(int(total_time))}"

            (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
            cv2.rectangle(img, (x1, y1), (x2, y2),(255,191,0), 2)
            cv2.rectangle(img, (x1, y1 - 20), (x1 + w, y1), (255,191,0), -1)
            cv2.putText(img, label, (x1, y1 - 5),cv2.FONT_HERSHEY_SIMPLEX, 0.6, 
            [255, 255, 255], 1)
            cv2.circle(img, data, 3, (255,191,0),-1)
        return img


    def start(self, camera_name=0):
        '''
        Stream processing

        When running a scenario - the caller can specify any specific camera.
        '''

        stream = camera_name

        print(f'Opening capture for {stream}')
        video = cv2.VideoCapture(stream)
        info_dic = {}
        sort_max_age = 5 
        sort_min_hits = 2
        sort_iou_thresh = 0.2
        sort_tracker = Track(max_age=sort_max_age,
                        min_hits=sort_min_hits,
                        iou_threshold=sort_iou_thresh) 

        prev_frame_time = time.time()
        new_frame_time = 0
        while True:
            # Do processing
            ret, frame = video.read()
            # fps = video.get(cv2.CAP_PROP_FPS)
            if ret is False:
                LOGGER.error('ERROR: reading from video frame')
                time.sleep(1)
                continue

            new_frame_time = time.time()
            fps = 1/(new_frame_time-prev_frame_time)
            # total_time += (new_frame_time-prev_frame_time)

            prev_frame_time = new_frame_time

            # Detect smoke & fire
            results = self.model(frame, size=640)  # batched inference

            det = results.xyxy[0]
            print("-----------------------------------")
            if len(det):
                dets_to_sort = np.empty((0,6))
                for x1,y1,x2,y2,conf,detclass in det.cpu().detach().numpy():
                    if int(detclass) == 0:
                        dets_to_sort = np.vstack((dets_to_sort, 
                                                np.array([x1, y1, x2, y2, 
                                                            conf, detclass])))

                tracked_dets = sort_tracker.update(dets_to_sort)

                if len(tracked_dets)>0:
                    bbox_xyxy = tracked_dets[:,:4]
                    identities = tracked_dets[:, 8]

                    for i in range(len(identities)):
                        id = identities[i]
                        bbox = bbox_xyxy[i]
                        if id in info_dic:
                            info_dic[id] = {
                                "id": int(id),
                                "count": info_dic[id]["count"] + 1,
                                "frames": info_dic[id]["frames"] + 1, 
                                "duration": round((info_dic[id]["duration"] + 1/fps), 2),
                                "bbox": list(bbox)
                            } 
                            self.draw_boxes(frame, [bbox], info_dic[id]['id'], info_dic[id]['duration'])  
                            if info_dic[id]["duration"] > self.alert_time:
                                self.f_event.fire_event(Event.CRITICAL, 'WEBCAM', "occupancy-monitoring", 'TIME-EXCEEDED', info_dic[id])         

                        else:
                            info_dic[id] = {"id": int(id), "count": 1, "frames": 1, "duration": 0, "bbox": list(bbox)}

                            self.draw_boxes(frame, [bbox], info_dic[id]['id'], info_dic[id]['duration'])                 
                                
                cv2.imshow('Output', frame)
                key = cv2.waitKey(5)
                if key == 27:
                    import sys
                    print('Exiting.')
                    sys.exit(0)
                        
            results.print()
            if self.stop_evt.is_set():
                break

def camera_stream():
    snf = OccupancyMonitoring(scenario_name = 'occupancy-monitoring')
    snf.start(camera_name=0)

if __name__ == '__main__':
    camera_stream()