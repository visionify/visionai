import os
import sys
from pathlib import Path
import unittest

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # visionai/visionai directory
PKGDIR = FILE.parents[2] # visionai dir
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

from util.general import WorkingDirectory, invoke_cmd
from config import VISIONAI_EXEC

class TestInvokeCliMain(unittest.TestCase):
    @WorkingDirectory(PKGDIR)
    def setUp(self):
        # Initialize visionai package before running tests
        output = invoke_cmd(f'{VISIONAI_EXEC} init')

    @WorkingDirectory(PKGDIR)
    def test_invoke_main(self):
        output = invoke_cmd(f'{VISIONAI_EXEC}')
        assert 'Error' in output
        assert 'Missing command' in output

    @WorkingDirectory(PKGDIR)
    def test_invoke_main_help(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} --help')
        assert 'VisionAI Toolkit' in output
        assert 'docs.visionify.ai' in output

    @WorkingDirectory(PKGDIR)
    def test_invoke_main_version(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} --version')
        assert 'VisionAI Toolkit Version' in output

    @WorkingDirectory(PKGDIR)
    def test_invoke_main_verbose(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} --verbose')
        assert 'Enabling verbose logging' in output

if __name__ == '__main__':
    unittest.main()
