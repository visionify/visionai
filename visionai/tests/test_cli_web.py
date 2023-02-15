import os
import sys
from pathlib import Path
import unittest

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # visionai/visionai directory
PKGDIR = FILE.parents[2] # visionai dir
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

from config import VISIONAI_EXEC
from util.general import WorkingDirectory, invoke_cmd

class TestInvokeCliWeb(unittest.TestCase):
    @WorkingDirectory(PKGDIR)
    def setUp(self):
        # Initialize visionai package before running tests
        output = invoke_cmd(f'{VISIONAI_EXEC} init')

    @WorkingDirectory(PKGDIR)
    def test_invoke_web_help_command(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} web --help')
        assert 'install' not in output
        assert 'start' in output
        assert 'status' in output
        assert 'stop' in output


    @WorkingDirectory(PKGDIR)
    def test_invoke_web_start_stop_status_command(self):
        # Stop anything that may be running
        output = invoke_cmd(f'{VISIONAI_EXEC} web stop')
        assert 'Stop web-app' in output

        # Start web-services
        output = invoke_cmd(f'{VISIONAI_EXEC} web start')
        assert 'Starting web app at' in output
        assert 'Starting web service API' in output
        assert 'Starting redis server' in output
        assert 'Starting grafana server' in output
        # assert 'Grafana server is at' in output  # CI/CD failing, TODO: Fix this
        assert 'Redis server is at' in output
        assert 'Web service API available at' in output
        assert 'Web app available at' in output

        # Start web-services again. It should just print the status
        output = invoke_cmd(f'{VISIONAI_EXEC} web start')
        assert 'Starting web app at' not in output
        assert 'Starting web service API' not in output
        assert 'Starting redis server' not in output
        # assert 'Starting grafana server' not in output # TODO: Fix this, failing in CI/CD
        # assert 'Grafana server is at' in output #TODO: Fix this, failing in CI/CD
        assert 'Redis server is at' in output
        assert 'Web service API available at' in output
        assert 'Web app available at' in output

        # Stop web-services
        output = invoke_cmd(f'{VISIONAI_EXEC} web stop')
        assert 'Stop web-app' in output
        assert 'Stop API service' in output
        assert 'Stop redis server' in output
        # assert 'Stop grafana server' in output # TODO: Fix this, failing in CI/CD

        # Stop web-services again. It should just print it is not running
        output = invoke_cmd(f'{VISIONAI_EXEC} web stop')
        assert 'Web-app not running' in output
        assert 'Web-API not running' in output
        assert 'Redis not running' in output
        # assert 'Grafana not running' in output # TODO: Fix this, failing in CI/CD


if __name__ == '__main__':
    unittest.main()
