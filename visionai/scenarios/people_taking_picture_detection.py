from rich import print
import time
import cv2
from PIL import Image


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

class PeopleTakingPictureDetection(Scenario):
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
    
    def dot(self, vA, vB):
        return vA[0]*vB[0]+vA[1]*vB[1]

    def ang(self, lineA, lineB):
        vA = [(lineA[0][0]-lineA[1][0]), (lineA[0][1]-lineA[1][1])]
        vB = [(lineB[0][0]-lineB[1][0]), (lineB[0][1]-lineB[1][1])]
        dot_prod = self.dot(vA, vB)
        magA = self.dot(vA, vA)**0.5
        magB = self.dot(vB, vB)**0.5
        cos_ = dot_prod/magA/magB
        angle = math.acos(dot_prod/magB/magA)
        ang_deg = math.degrees(angle)%360
        if ang_deg-180>=0:
            return 360 - ang_deg
        else: 
            return ang_deg

    def draw_box(self, image, land_marks):
        cv2.line(image, land_marks[11], land_marks[12], self.color, self.thickness)
        cv2.line(image, land_marks[11], land_marks[23], self.color, self.thickness)
        cv2.line(image, land_marks[12], land_marks[24], self.color, self.thickness)
        cv2.line(image, land_marks[23], land_marks[24], self.color, self.thickness)
        cv2.line(image, land_marks[23], land_marks[25], self.color, self.thickness)
        cv2.line(image, land_marks[24], land_marks[26], self.color, self.thickness)
        cv2.line(image, land_marks[25], land_marks[27], self.color, self.thickness)
        cv2.line(image, land_marks[26], land_marks[28], self.color, self.thickness)
        cv2.line(image, land_marks[11], land_marks[13], self.color, self.thickness)
        cv2.line(image, land_marks[13], land_marks[15], self.color, self.thickness)
        cv2.line(image, land_marks[14], land_marks[16], self.color, self.thickness)
        cv2.line(image, land_marks[12], land_marks[14], self.color, self.thickness)
        return image

    def slope(self, x, y):
        if(y[0] - x[0] != 0):
            return (float)(y[1]-x[1])/(y[0]-x[0])
        return 0.0

    def find_angle(self, land_marks):
        ind = [[24,12,14,16],[23,11,13,15]]
        angles = []
        slopee = []
        for n in range(0,len(ind)):
            left_index = ind[n]
            for i in range(0,len(ind[0])-2):
                angles.append(180 - self.ang([land_marks[left_index[i]],land_marks[left_index[i+1]]], [land_marks[left_index[i+1]],land_marks[left_index[i+2]]]))
        return angles
    
    def mobile_check(self, mobile_centeroid, xyxy, im0shape):
        w,h,_ = im0shape
        for m in mobile_centeroid:
            if m[0] > (xyxy[0]) and m[0] < (xyxy[2]) and m[1] > (xyxy[1]) and m[1] < (xyxy[3]):
                return m
            else:
                return []

    def find_height(self, land_marks):
        top_point = [0,5,8,10]
        bottom_point = [26,28,30,32]
        height = 0
        for h in range(0,3):
            try:
                height = land_marks[bottom_point[h]][1] - land_marks[top_point[h]][1]
                # print("preson height in loop : ",height)
                break
            except:
                continue
        return height

    def frame_edit(self, im0):
        vision_image = cv2.imread("visionify.jpg") # image size = 107x29
        im0[25:54,25:132] = vision_image
        # im0[0:65, 880:1279] = cv2.medianBlur(im0[0:65, 880:1279],35)
        return im0

    def start(self, camera_name=0):
        '''
        Stream processing

        When running a scenario - the caller can specify any specific camera.
        '''

        import cv2
        stream = camera_name
        # stream = "F:\\visionify\\test-videos\\box_moving_w_halmet.MOV"

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
            centroid = []
            top_center = []
            device = 'cpu'
            results = self.model(image, size=640) #, visualize=False)
            stride, names= self.model.stride, self.model.names
            im0 = image
            im0shape = im0.shape
            seen = 0
            det = results.xyxy[0]
            seen += 1
            annotator = Annotator(im0, line_width=self.line_thickness) #, example=str(names))
            person_count = 0
            if len(det):
                count_i = 0
                mobile_centeroid = []
                param = {"person_id": [], "pose_points":[], "dim":[], "mobile_centeroid": []}
                for *xyxy, conf, cls in reversed(det):
                    c = int(cls)  # integer class
                    label = f'{names[c]} {conf:.2f}'
                    if 'class67' in label:
                        annotator.box_label(xyxy, label)
                        wi = int(xyxy[0]) + int(int(xyxy[2] - xyxy[0])/2)
                        hi = int(xyxy[1]) + int(int(xyxy[3] - xyxy[1])/2)
                        mobile_centeroid.append([int(xyxy[0]),int(xyxy[3])]) # +int(wi/2)
                for *xyxy, conf, cls in reversed(det):
                    c = int(cls)  # integer class
                    label = f'{names[c]} {conf:.2f}'
                    if 'class0' in label:
                        person_status = "Normal"
                        crop = im0[int(xyxy[1]):int(xyxy[3]),int(xyxy[0]):int(xyxy[2])]
                        mobile = self.mobile_check(mobile_centeroid, xyxy, im0shape)
                        param["person_id"].append(person_count)
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
                                    # cv2.circle(crop, (cx,cy), 3, (240,0,0), cv2.FILLED)
                                    land_marks.append([cx,cy])
                                if land_marks != []:
                                    crop = self.draw_box(crop, land_marks)
                                    slopeangle = self.find_angle(land_marks)
                                    right_angel_w_s_l = slopeangle[0]
                                    right_angel_s_l_w = slopeangle[1]
                                    left_angel_w_s_l = slopeangle[2]
                                    left_angel_s_l_w = slopeangle[3]
                                    if mobile:
                                        mobile_to_left_hand_dist = math.dist((mobile[0]-int(xyxy[0]), mobile[1]-int(xyxy[1])), land_marks[15])
                                        mobile_to_right_hand_dist = math.dist((mobile[0]-int(xyxy[0]), mobile[1]-int(xyxy[1])), land_marks[16])
                                    if left_angel_w_s_l > 35: # checking for left hand
                                        if right_angel_w_s_l > 35: # checking for right hand
                                            if mobile:
                                                if left_angel_s_l_w > 125 and right_angel_s_l_w > 100 and mobile_to_left_hand_dist < 350 and mobile_to_right_hand_dist < 350:
                                                    cv2.putText(crop, "taking picture", (0,20) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
                                                    self.f_event.fire_event(Event.WARNING, 'OFFICE-01', 'people-taking-picture-detection', 'TAKING_PICTURE', {})
                                                elif right_angel_s_l_w > 55 and mobile_to_right_hand_dist < 350:
                                                    cv2.putText(crop, "taking picture", (0,20) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
                                                    self.f_event.fire_event(Event.WARNING, 'OFFICE-01', 'people-taking-picture-detection', 'TAKING_PICTURE', {})
                                                elif left_angel_s_l_w > 125 and mobile_to_left_hand_dist < 350:
                                                    cv2.putText(crop, "taking picture", (0,20) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
                                                    self.f_event.fire_event(Event.WARNING, 'OFFICE-01', 'people-taking-picture-detection', 'TAKING_PICTURE', {})
                                                else:
                                                    cv2.putText(crop, "taking picture", (0,20) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
                                                    self.f_event.fire_event(Event.WARNING, 'OFFICE-01', 'people-taking-picture-detection', 'TAKING_PICTURE', {})
                                            else:
                                                cv2.putText(crop, "Not taking picture", (0,20) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA) 
                                                self.f_event.fire_event(Event.INFO, 'OFFICE-01', 'people-taking-picture-detection', 'NOT_TAKING_PICTURE', {})    
                                        else:
                                            if mobile:
                                                if left_angel_s_l_w > 125 and mobile_to_left_hand_dist < 350:
                                                    cv2.putText(crop, "taking picture", (0,20) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
                                                    self.f_event.fire_event(Event.WARNING, 'OFFICE-01', 'people-taking-picture-detection', 'TAKING_PICTURE', {})
                                                else:
                                                    cv2.putText(crop, "taking picture", (0,20) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
                                                    self.f_event.fire_event(Event.WARNING, 'OFFICE-01', 'people-taking-picture-detection', 'TAKING_PICTURE', {})
                                            else:
                                                cv2.putText(crop, "Not taking picture", (0,20) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
                                                self.f_event.fire_event(Event.INFO, 'OFFICE-01', 'people-taking-picture-detection', 'NOT_TAKING_PICTURE', {})
                                    else:
                                        if right_angel_w_s_l > 35: # checking for right hand
                                            if mobile:
                                                if right_angel_s_l_w > 55 and mobile_to_right_hand_dist < 350:
                                                    cv2.putText(crop, "taking pictures", (0,20) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
                                                    self.f_event.fire_event(Event.WARNING, 'OFFICE-01', 'people-taking-picture-detection', 'TAKING_PICTURE', {})
                                                else:
                                                    cv2.putText(crop, "taking pictures", (0,20) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
                                                    self.f_event.fire_event(Event.WARNING, 'OFFICE-01', 'people-taking-picture-detection', 'TAKING_PICTURE', {})
                                        else:
                                            cv2.putText(crop, "Not taking pictures", (0,20) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
                                            self.f_event.fire_event(Event.INFO, 'OFFICE-01', 'people-taking-picture-detection', 'NOT_TAKING_PICTURE', {})
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


def people_taking_picture_detection():
    snf = PeopleTakingPictureDetection(scenario_name = 'phone-detection')
    # snf.load_model()
    imgs = [
    cv2.imread("visionai/models/data/images/ergo_test_1.png"),
    cv2.imread("visionai/models/data/images/ptp7.jpg"),
    cv2.imread("visionai/models/data/images/ptp8.jpg"),
    cv2.imread("visionai/models/data/images/fall_1.jpg"),
    # img = Image.open('visionai/models/data/images/no_fall.jpg')
    # img = Path('visionai/models/data/images/no_fall.jpg')
    ]
    for idx, img in enumerate(imgs):
        img  = snf.process_image(img)
        cv2.imwrite(str(idx) +'sfd_res_2.jpg', img)


def camera_stream():
    snf = PeopleTakingPictureDetection(scenario_name = 'people-taking-picture-detection')
    snf.start(camera_name=0)

if __name__ == '__main__':
    # people_taking_picture_detection()
    camera_stream()