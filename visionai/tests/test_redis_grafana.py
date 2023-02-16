import os
import sys
from pathlib import Path
import unittest
import docker
import pytest

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # visionai/visionai directory
PKGDIR = FILE.parents[2] # visionai dir
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

from config import *
from util.docker_utils import *
from util.general import WorkingDirectory, invoke_cmd



class TestRedis(unittest.TestCase):

    @pytest.mark.skip(reason="Grafana keeps failing on CI/CD. Skipping for now.")
    def test_redis_grafana_functions(self):
        # Stop any priori containers
        redis_container_stop()
        grafana_container_stop()

        # Start containers
        redis_container_start()
        grafana_container_start()

        # Install redis python package
        redis_python_install()

        # Validate redis python package installed
        assert redis_python_package_installed(), 'Redis python package is not installed.'

        # Check if containers is running
        assert docker_container_is_running(container_name=REDIS_CONTAINER_NAME), 'Redis container is not running.'
        assert docker_container_is_running(container_name=GRAFANA_CONTAINER_NAME), 'Grafana container is not running.'

        # Check if network is created
        assert docker_network_is_running(network_name=DOCKER_NETWORK), 'Docker network is not created.'


        # Check containers are joined to that network
        client = docker.from_env()
        container = client.containers.get(REDIS_CONTAINER_NAME)
        networks = container.attrs['NetworkSettings']['Networks']
        redis_network_joined = False
        if networks:
            for network_name, network_config in networks.items():
                if network_name == DOCKER_NETWORK:
                    redis_network_joined = True

        container = client.containers.get(GRAFANA_CONTAINER_NAME)
        networks = container.attrs['NetworkSettings']['Networks']
        grafana_network_joined = False
        if networks:
            for network_name, network_config in networks.items():
                if network_name == DOCKER_NETWORK:
                    grafana_network_joined = True

        assert redis_network_joined, f'Redis container is not joined to network {DOCKER_NETWORK}'
        assert grafana_network_joined, f'Grafana container is not joined to network {DOCKER_NETWORK}'

        # Stop the containers
        redis_container_stop()
        grafana_container_stop()

        # Ensure containers are stopped
        assert docker_container_is_running(container_name=REDIS_CONTAINER_NAME) == False, 'Redis container is still running.'
        assert docker_container_is_running(container_name=GRAFANA_CONTAINER_NAME) == False, 'Grafana container is still running.'


if __name__ == '__main__':
    unittest.main()


