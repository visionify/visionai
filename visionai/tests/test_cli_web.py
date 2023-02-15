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
        assert 'Starting web service API at port' in output
        assert 'API endpoint available at:' in output
        assert 'Starting web app at port' in output
        assert 'Webapp available at:' in output

        # Start web-services again. It should just print the status
        output = invoke_cmd(f'{VISIONAI_EXEC} web start')
        assert 'Web server already running at:' in output
        assert 'API server already running at:' in output

        # Stop web-services
        output = invoke_cmd(f'{VISIONAI_EXEC} web stop')
        assert 'Stop web-app' in output
        assert 'Stop API service' in output

        # Stop web-services again. It should just print it is not running
        output = invoke_cmd(f'{VISIONAI_EXEC} web stop')
        assert 'Web-server not running' in output


if __name__ == '__main__':
    unittest.main()
