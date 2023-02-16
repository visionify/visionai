import sys
from urllib.parse import urlparse
from pathlib import Path
import importlib
from abc import ABC, abstractmethod
from threading import Thread, Event

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # visionai/visionai directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

from util import TryExcept
from util.general import colorstr, get_system_version, LOGGER, gpu_mem_stats
from config import TRITON_HTTP_URL

class Scenario(ABC):
    def __init__(self, scenario_name, camera_name=0, events=None, triton_url=TRITON_HTTP_URL):
        '''
        Initialize scenario base object.
        '''
        self.scenario_name = scenario_name
        self.camera_name = camera_name
        self.events = events
        self.triton_url = triton_url
        self.stop_evt = Event()

    @abstractmethod
    def start(self, stream=None):
        '''
        Process a camera stream/image/file/web-cam stream

        Implement each scenario as a blocking call. It would be
        called as a thread from the calling process.

        Implement support for handing if stop_evt is set.

        while True:
            # Do processing
            # ...

            # if stop_evt is set, then break
            if self.stop_evt.is_set():
                break

        '''
        pass

    def stop(self):
        '''
        Stop the infernece engine

        This is called when start has been called within a thread etc.
        '''
        self.stop_evt.set()


def load_scenario(scenario_name, camera_name=None, events=None, triton_url=TRITON_HTTP_URL):
    '''
    Load the scenario inference object

    Dynamically identify what is the inference class name based
    on scenario_name and load an object of that class.
    scenario    : smoke-and-fire-detection
    filename    : scenarios/smoke_and_fire_detection.py
    module name : smoke_and_fire_detection
    class name  : SmokeAndFireDetection
    '''

    moduleName = scenario_name.replace('-', '_')
    className  = ''.join(x.capitalize() for x in moduleName.split('_'))
    moduleName = 'scenarios.' + moduleName

    my_module = importlib.import_module(moduleName)
    my_class = getattr(my_module, className)

    # Print remaining GPU memory here.
    LOGGER.info(f'🚀 Loading scenario for {colorstr(scenario_name)}')
    gpu_mem = gpu_mem_stats()
    if gpu_mem < 30:
        LOGGER.warning('⛔ Running low on GPU memory')

    # Create inference object
    # This would be an object with Scenario base class.
    my_object = my_class(scenario_name=scenario_name, camera_name=camera_name, events=events, triton_url=triton_url)
    return my_object

