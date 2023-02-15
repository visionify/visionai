from rich import print
import time
import cv2
from PIL import Image
import numpy as np
import math
from math import atan
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

class ErgonomicsDetection(Scenario):
    model = None
    conf_thres=0.25  # confidence threshold
    iou_thres=0.45  # NMS IOU threshold
    classes=None  # filter by class: --class 0, or --class 0 2 3
    agnostic_nms=False  # class-agnostic NMS
    max_det=1000  # maximum detections per image
    line_thickness=3  # bounding box thickness (pixels)
    color = (0, 200, 0)
    thickness = 1 
    device='cpu'  # cuda device, i.e. 0 or 0,1,2,3 or cpu

    def __init__(self, scenario_name, camera_name=0, events=None, triton_url=TRITON_HTTP_URL):
        self.up_count = 0
        self.down_count = 0
        self.up_counter = True
        self.down_counter = False
        from util.general import check_requirements
        check_requirements('mediapipe', install=True)
        import mediapipe as mp
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_pose = mp.solutions.pose
        self.f_event =  EventsEngine(use_redis=True)
        from models.triton_client_yolov5 import yolov5_triton
        self.model = yolov5_triton('http://localhost:8000', scenario_name)
        super().__init__(scenario_name, camera_name, events, triton_url)

    def land_3d(self, landmarks_3d):
        left_shoulder = np.array([landmarks_3d.landmark[11].x, landmarks_3d.landmark[11].y, landmarks_3d.landmark[11].z])
        right_shoulder = np.array([landmarks_3d.landmark[12].x, landmarks_3d.landmark[12].y, landmarks_3d.landmark[12].z])
        left_hip = np.array([landmarks_3d.landmark[23].x, landmarks_3d.landmark[23].y, landmarks_3d.landmark[23].z])
        right_hip = np.array([landmarks_3d.landmark[24].x, landmarks_3d.landmark[24].y, landmarks_3d.landmark[24].z])
        left_knee = np.array([landmarks_3d.landmark[25].x, landmarks_3d.landmark[25].y, landmarks_3d.landmark[25].z])
        right_knee = np.array([landmarks_3d.landmark[26].x, landmarks_3d.landmark[26].y, landmarks_3d.landmark[26].z])
        left_ankle = np.array([landmarks_3d.landmark[27].x, landmarks_3d.landmark[27].y, landmarks_3d.landmark[27].z])
        right_ankle = np.array([landmarks_3d.landmark[28].x, landmarks_3d.landmark[28].y, landmarks_3d.landmark[28].z])
        mid_shoulder = (left_shoulder + right_shoulder) / 2
        mid_hip = (left_hip + right_hip) / 2
        mid_knee = (left_knee + right_knee) / 2
        mid_ankle = (left_ankle + right_ankle) / 2
        s_w_k_angle = self.get_angle(mid_knee, mid_hip, mid_shoulder, mid_hip, adjust=True)
        w_k_a_angle = self.get_angle(mid_ankle, mid_knee, mid_hip, mid_knee, adjust=True)
        return s_w_k_angle, w_k_a_angle

    def get_angle(self, a, b, c, d, adjust):
        """return the angle between two vectors"""
        vec1 = a - b
        vec2 = c - d

        cosine_angle = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
        angle = np.arccos(cosine_angle)
        if (adjust):
            angle_adjusted = abs(np.degrees(angle) - 180)
            return int(angle_adjusted)
        else:
            return int(abs(np.degrees(angle)))

    def point_check(self, dim, p) : # bl, tr bottom_left, top_right, point
        bl = [dim[0],dim[3]]
        tr = [dim[2],dim[1]]
        # print(bl, tr, p)
        if (p[0] > bl[0] and p[0] < tr[0] and p[1] < bl[1] and p[1] > tr[1]) :
            return True
        else :
            return False

    def findAngle(self, M1, M2):
        try:
            PI = 3.14159265
            angle = abs((M2 - M1) / (1 + M1 * M2))
            ret = atan(angle)
            val = (ret * 180) / PI
            return round(val, 4)
        except:
            return 0.0

    def draw_box(self, image, land_marks):
        cv2.line(image, land_marks[11], land_marks[12], self.color, self.thickness)
        cv2.line(image, land_marks[11], land_marks[23], self.color, self.thickness)
        cv2.line(image, land_marks[12], land_marks[24], self.color, self.thickness)
        cv2.line(image, land_marks[23], land_marks[24], self.color, self.thickness)
        cv2.line(image, land_marks[23], land_marks[25], self.color, self.thickness)
        cv2.line(image, land_marks[24], land_marks[26], self.color, self.thickness)
        cv2.line(image, land_marks[25], land_marks[27], self.color, self.thickness)
        cv2.line(image, land_marks[26], land_marks[28], self.color, self.thickness)
        return image

    def slope(self, x, y):
        if(y[0] - x[0] != 0):
            return (float)(y[1]-x[1])/(y[0]-x[0])
        return 0.0

    def find_angle(self, land_marks):
        ind = [[11,27,2,23],[5,12,24,28]]
        angles = []
        slopee = []
        sl = self.slope(land_marks[11],land_marks[27])
        ag = self.findAngle(sl, 0)
        return ag


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
            start_time = time.time()
            text_font = 1
            text_thickness = 1
            centroid = []
            top_center = []
            # Load model
            device = 'cpu'
            results = self.model(image, size=640) #, visualize=False)
            stride, names= self.model.stride, self.model.names
            im0 = image
            seen = 0
            det = results.xyxy[0]
            # seen += 1
            annotator = Annotator(im0, line_width=self.line_thickness) #, example=str(names))
            person_count = 0
            if len(det):
                count_i = 0
                param = {"person_id": [], "pose_points":[], "dim":[], "mobile_centeroid": []}
                for *xyxy, conf, cls in reversed(det):
                    c = int(cls)  # integer class
                    label = f'{names[c]} {conf:.2f}'
                    # print("Detected labels : ", label)
                    if 'class0' in label:
                        person_status = "Normal"
                        crop = im0[int(xyxy[1]):int(xyxy[3]),int(xyxy[0]):int(xyxy[2])]
                        # param["person_id"].append(person_count)
                        with self.mp_pose.Pose(
                            min_detection_confidence=0.5,
                            min_tracking_confidence=0.5) as pose:
                            crop = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
                            results = pose.process(crop)
                            crop= cv2.cvtColor(crop, cv2.COLOR_RGB2BGR)
                            land_marks = []
                            if results.pose_landmarks:
                                for idx, pose_marks in enumerate(results.pose_landmarks.landmark):
                                    h,w = int(xyxy[3]-xyxy[1]), int(xyxy[2]-xyxy[0])
                                    cx,cy = int(pose_marks.x * w) , int(pose_marks.y * h)
                                    land_marks.append([cx,cy])
                                if land_marks != []:
                                    crop = self.draw_box(crop, land_marks)
                                    landmark_3d = results.pose_world_landmarks
                                    mid_s_w_k_angle, mid_w_k_a_angle = self.land_3d(landmark_3d)
                                    # slopeangle = self.find_angle(land_marks)
                                    if mid_s_w_k_angle > 75  and self.down_counter == True:
                                        self.down_count = self.down_count+1
                                        self.up_counter = True
                                        self.down_counter = False
                                    elif mid_s_w_k_angle < 75 and self.up_counter == True:
                                        if self.up_counter == True:
                                            self.up_count = self.up_count+1
                                            self.up_counter = False
                                            self.down_counter = True
                                    cv2.putText(crop, "BdCnt:" + str(self.down_count), (0,50) , cv2.FONT_HERSHEY_SIMPLEX, text_font, (0,0,250), text_thickness, cv2.LINE_AA)
                                    self.f_event.fire_event(Event.INFO, 'OFFICE-01', 'ergonomics-detection', 'BENDING_COUNT', {"Bending Count" : self.down_count})
                                    im0[int(xyxy[1]):int(xyxy[3]),int(xyxy[0]):int(xyxy[2])] = crop
                            param["pose_points"].append(land_marks)
                            param["dim"].append([int(xyxy[0]),int(xyxy[1]),int(xyxy[2]),int(xyxy[3])])
                            annotator.box_label(xyxy, label)
                        person_count+=1
                im0 = annotator.result()
            if self.stop_evt.is_set():
                    break
            cv2.imshow('detection', im0)
            if cv2.waitKey(5) & 0xFF == 27:
                break
        video.release()
        cv2.destroyAllWindows()

def ergonomics_detection():
    snf = ErgonomicsDetection(scenario_name = 'phone-detection')
    # snf.load_model()
    img = cv2.imread("visionai/models/data/images/fall_12.png")
    # img = Image.open('visionai/models/data/images/no_fall.jpg')
    # img = Path('visionai/models/data/images/no_fall.jpg')
    img  = snf.process_image(img)
    cv2.imwrite('sfd_res_2.jpg', img)

def camera_stream():
    snf = ErgonomicsDetection(scenario_name = 'ergonomics-detection')
    snf.start(camera_name=0)

if __name__ == '__main__':
    # people_taking_picture_detection()
    camera_stream()

