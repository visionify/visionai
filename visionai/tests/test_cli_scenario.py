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

class TestInvokeCliScenario(unittest.TestCase):
    @WorkingDirectory(PKGDIR)
    def setUp(self):
        # Initialize visionai package before running tests
        output = invoke_cmd(f'{VISIONAI_EXEC} init')

    @WorkingDirectory(PKGDIR)
    def test_invoke_scenario(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} scenario')
        assert 'Error' in output
        assert 'Missing command' in output

    @WorkingDirectory(PKGDIR)
    def test_invoke_scenario_help(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} scenario --help')
        assert 'Usage' in output
        assert 'Commands' in output
        assert 'download' in output
        assert 'list' in output
        assert 'test' in output

    @WorkingDirectory(PKGDIR)
    def test_list_all_scenarios(self):
        # list scenario
        output = invoke_cmd(f'{VISIONAI_EXEC} scenario list')
        assert 'smoke-and-fire-detection' in output
        assert 'ppe-detection' in output
        assert 'docs.visionify.ai' in output
        assert 'Categories' in output
        assert 'Tags' in output
        assert 'Acc:' in output
        assert 'Rec:' in output
        assert 'F1:' in output
        assert 'Size:' in output

    @WorkingDirectory(PKGDIR)
    def test_download_specific_scenario(self):
        # download specific scenario
        output = invoke_cmd(f'{VISIONAI_EXEC} scenario download smoke-and-fire-detection')
        assert 'download_models' in output
        assert 'Model: smoke-and-fire-detection' in output

    @WorkingDirectory(PKGDIR)
    def test_download_all_scenarios(self):
        # download all scenarios
        output = invoke_cmd(f'{VISIONAI_EXEC} scenario download all')
        assert 'Downloading all configured scenarios' in output

    # This requires a prompt from user. Skipping it in unit-tests.
    # @WorkingDirectory(PKGDIR)
    # def test_download_world_scenarios(self):
    #     # download all scenarios
    #     output = invoke_cmd(f'{VISIONAI_EXEC} scenario download world')
    #     assert 'Downloading all available (world) scenarios' in output


if __name__ == '__main__':
    unittest.main()
