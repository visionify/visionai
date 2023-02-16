import os
import datetime
import json
from enum import Enum
import time

import sys
from pathlib import Path
FILE = Path(__file__).resolve()
SCENARIOS = FILE.parents[0]
ROOT = FILE.parents[1]  # Root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from rich import print, print_json
from util.general import check_requirements
from util.docker_utils import redis_container_start, redis_python_install

class Event(str, Enum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'

class EventsEngine():
    def __init__(self, use_redis:bool=False, use_event_hub:bool=False, use_log:bool=True):
        self.use_redis = use_redis
        self.use_event_hub = use_event_hub
        self.use_log = use_log

        # Initialize redis if needed
        if self.use_redis:
            redis_container_start()
            redis_python_install()

            import redis
            self.redis_client = redis.Redis(host='localhost', port=6379, db=0)

            # listen to self events for validation
            self.redis_pubsub = self.redis_client.pubsub(ignore_subscribe_messages=True)
            self.redis_pubsub.subscribe('visionai')

    def fire_event(
        self,
        event_type: Event = Event.INFO,
        camera:str = 'CAMERA??',
        scenario: str = 'SCENARIO??',
        event_name = 'EVENT??',
        event_data = None
        ):

        if self.use_log:
            # Log the event to stdout.
            timestr = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if event_type == Event.DEBUG:
                clr = 'cyan'
            elif event_type == Event.INFO:
                clr = 'blue'
            elif event_type == Event.WARNING:
                clr = 'yellow'
            elif event_type == Event.ERROR:
                clr = 'dark_red'
            elif event_type == Event.CRITICAL:
                clr = 'bold red'
            else:
                clr = 'grey'

            print(f'[[{clr}]{timestr}[/{clr}]] [[{clr}]{camera}[/{clr}]] [[{clr}]{scenario}[/{clr}]]: [{clr}]{event_name}[/{clr}]')
            print_json(data=event_data)

        if self.use_redis:
            # Log the event to redis
            event_data.update({
                'event_type': event_type,
                'camera': camera,
                'scenario': scenario,
                'event_name': event_name,
                'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

            # Send event to "events" channel
            self.redis_client.publish('visionai', json.dumps(event_data))

        if self.use_event_hub:
            # Send the event to Azure Event Hub
            pass

    def print_received_messages(self):
        if self.use_redis:
            print('Got messages:')
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - ')
            start_time = time.time()
            stop_time = start_time + 2
            while time.time() < stop_time:
                message = self.redis_pubsub.get_message(timeout=1)
                if message is None:
                    time.sleep(0.1)
                    continue

                event_data = json.loads(message['data'])
                print(event_data)
                time.sleep(0.1)
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - ')

if __name__ == '__main__':

    ev = {
    "version": "0.1",
    "cameras": [
        {
        "id": "581700a9-fb09-4f23-b8b9-abf371930e84",
        "name": "OFFICE-01",
        "uri": "https://youtu.be/whlymAuRtzU",
        "events": "all",
        "preprocess": [
            "face-blurring"
        ],
        "scenarios": [
            "ppe-detection",
            "smoke-and-fire-detection"
        ]
        },
        {
        "id": "581700a9-fb09-4f23-b8b9-abf371930e84",
        "name": "OFFICE-02",
        "uri": "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4",
        "events": "critical",
        "preprocess": [
            "face-blurring"
        ],
        "scenarios": [
            "smoke-and-fire-detection"
        ]
        }
    ]
    }


    ee = EventsEngine(use_redis=True)

    while True:
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        ee.fire_event(Event.DEBUG, 'OFFICE-01', 'ppe-detection', 'PERSON_WITHOUT_HELMET', ev)
        ee.fire_event(Event.INFO, 'OFFICE-01', 'ppe-detection', 'PERSON_WITHOUT_HELMET', ev)
        ee.fire_event(Event.WARNING, 'OFFICE-01', 'ppe-detection', 'PERSON_WITHOUT_HELMET', ev)
        ee.fire_event(Event.ERROR, 'OFFICE-01', 'ppe-detection', 'PERSON_WITHOUT_HELMET', ev)
        ee.fire_event(Event.CRITICAL, 'OFFICE-01', 'ppe-detection', 'PERSON_WITHOUT_HELMET', ev)

        # ee.print_received_messages()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - ')

        time.sleep(1)

