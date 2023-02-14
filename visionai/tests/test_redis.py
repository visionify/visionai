import os
import sys
from pathlib import Path
import unittest

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # visionai/visionai directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

from config import REDIS_ENABLED
from util.docker_utils import docker_conatiner_is_running
from util.redis_utils import redis_container_start, redis_container_stop, redis_python_install, redis_python_package_installed

class TestRedis(unittest.TestCase):
    def setUp(self) -> None:
        redis_container_start()

    # def tearDown(self) -> None:
    #     redis_container_stop()

    def test_redis_functions(self):

        # Start redis container
        redis_container_start()

        # Install package
        redis_python_install()

        if REDIS_ENABLED:
            # Check if container is running
            assert docker_conatiner_is_running(container_name='redis'), 'Redis container is not running.'

            # Validate redis python package installed
            assert redis_python_package_installed(), 'Redis python package is not installed.'
        else:
            assert True, 'Redis is not enabled. Skipping validation.'



if __name__ == '__main__':
    unittest.main()


