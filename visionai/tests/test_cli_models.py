import os
import sys
from pathlib import Path
import unittest

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1] # visionai/visionai
PKGDIR = FILE.parents[2] # visionai folder
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

from config import VISIONAI_EXEC
from util.general import WorkingDirectory, invoke_cmd

class TestInvokeCliModels(unittest.TestCase):
    @WorkingDirectory(PKGDIR)
    def setUp(self):
        # Initialize visionai package before running tests
        output = invoke_cmd(f'{VISIONAI_EXEC} init')

    @WorkingDirectory(PKGDIR)
    def test_invoke_models_status(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} models status')
        assert 'Models status' in output

    @WorkingDirectory(PKGDIR)
    def test_invoke_models_start(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} models start')
        assert 'Start models' in output

    @WorkingDirectory(PKGDIR)
    def test_invoke_models_start(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} models serve')
        assert 'Start models' in output

    @WorkingDirectory(PKGDIR)
    def test_invoke_models_stop(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} models stop')
        assert 'Stop models' in output

if __name__ == '__main__':
    unittest.main()
