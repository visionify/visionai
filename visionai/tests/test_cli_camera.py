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

class TestInvokeCliCamera(unittest.TestCase):
    @WorkingDirectory(PKGDIR)
    def setUp(self):
        # Initialize visionai package before running tests
        output = invoke_cmd(f'{VISIONAI_EXEC} init')

    @WorkingDirectory(PKGDIR)
    def test_invoke_camera(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} camera')
        assert 'Error' in output
        assert 'Missing command' in output

    @WorkingDirectory(PKGDIR)
    def test_invoke_camera_help(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} camera --help')
        assert 'Usage' in output
        assert 'Commands' in output
        assert 'add' in output
        assert 'list' in output
        assert 'remove' in output

    @WorkingDirectory(PKGDIR)
    def test_invoke_camera_add_help(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} camera add --help')
        assert 'Usage' in output
        assert 'camera' in output
        assert 'add' in output
        assert '--name' in output
        assert '--uri' in output
        assert '--description' in output
        assert '--help' in output

    @WorkingDirectory(PKGDIR)
    def test_invoke_camera_add_remove(self):
        # cleanup prior configuration
        output = invoke_cmd(f'{VISIONAI_EXEC} camera reset --confirm')

        # add camera
        output = invoke_cmd(f'{VISIONAI_EXEC} camera add --name TEST-999 --uri youtube.com --description "Test camera"')
        assert 'Success' in output

        # list camera
        output = invoke_cmd(f'{VISIONAI_EXEC} camera list')
        assert "'name': 'TEST-999'" in output
        assert "'uri': 'youtube.com'" in output

        # remove camera
        output = invoke_cmd(f'{VISIONAI_EXEC} camera remove --name TEST-999')
        assert 'Success' in output

        # list camera
        output = invoke_cmd(f'{VISIONAI_EXEC} camera list')
        assert "'name': 'TEST-999'" not in output

    @WorkingDirectory(PKGDIR)
    def test_invoke_camera_add_scenario_help(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} camera add-scenario --help')
        assert 'Usage' in output
        assert 'scenario' in output
        assert 'add' in output
        assert '--camera' in output
        assert '--scenario' in output
        assert '--help' in output

    @WorkingDirectory(PKGDIR)
    def test_invoke_camera_remove_scenario_help(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} camera remove-scenario --help')
        assert 'Usage' in output
        assert 'scenario' in output
        assert 'remove' in output
        assert '--scenario' in output
        assert '--camera' in output
        assert '--help' in output

    @WorkingDirectory(PKGDIR)
    def test_invoke_camera_list_scenario_help(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} camera list-scenario --help')
        assert 'Usage' in output
        assert 'scenario' in output
        assert '--camera' in output
        assert '--help' in output

    @WorkingDirectory(PKGDIR)
    def test_invoke_camera_list_scenarios_help(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} camera list-scenarios --help')
        assert 'Usage' in output
        assert 'scenario' in output
        assert '--camera' in output
        assert '--help' in output

    @WorkingDirectory(PKGDIR)
    def test_invoke_camera_list_scenarios_all(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} camera list-scenarios')
        assert 'scenarios for all cameras' in output.lower()

    @WorkingDirectory(PKGDIR)
    def test_invoke_camera_list_scenario_all(self):
        output = invoke_cmd(f'{VISIONAI_EXEC} camera list-scenario')
        assert 'scenarios for all cameras' in output.lower()

    @WorkingDirectory(PKGDIR)
    def test_invoke_camera_list_scenario_for_camera(self):
        # reset all cameras
        output = invoke_cmd(f'{VISIONAI_EXEC} camera reset --confirm')

        # add camera
        output = invoke_cmd(f'{VISIONAI_EXEC} camera add --name TEST-999 --uri youtube.com --description "Test camera"')
        assert 'Success' in output

        # add scenarios for camera
        output = invoke_cmd(f'{VISIONAI_EXEC} camera add-scenario --camera TEST-999 --scenario smoke-and-fire-detection')
        assert 'Scenario smoke-and-fire-detection successfully added for camera TEST-999' in output
        output = invoke_cmd(f'{VISIONAI_EXEC} camera add-scenario --camera TEST-999 --scenario ppe-detection')
        assert 'Scenario ppe-detection successfully added for camera TEST-999' in output

        # list cameras for scenario
        output = invoke_cmd(f'{VISIONAI_EXEC} camera list-scenarios --camera TEST-999')
        assert "'name': 'smoke-and-fire-detection'" in output
        assert "'name': 'ppe-detection'" in output
        assert "scenarios for camera: TEST-999" in output

        # reset everything
        output = invoke_cmd(f'{VISIONAI_EXEC} camera reset --confirm')
        assert 'Camera configuration reset' in output

    @WorkingDirectory(PKGDIR)
    def test_invoke_camera_scenario_add_remove_list(self):
        # cleanup (prior test failures)
        output = invoke_cmd(f'{VISIONAI_EXEC} camera reset --confirm')

        # add camera
        output = invoke_cmd(f'{VISIONAI_EXEC} camera add --name TEST-999 --uri youtube.com --description "Test camera"')
        assert 'Successfully added camera: TEST-999' in output

        # add scenario
        output = invoke_cmd(f'{VISIONAI_EXEC} camera add-scenario --camera TEST-999 --scenario smoke-and-fire-detection')
        assert 'Scenario' in output
        assert 'smoke-and-fire-detection' in output
        assert 'added for camera' in output

        # list scenario
        output = invoke_cmd(f'{VISIONAI_EXEC} camera list-scenario --camera TEST-999')
        assert "scenarios for camera" in output
        assert "'cam': 'TEST-999'" in output
        assert "'name': 'smoke-and-fire-detection'" in output

        # remove scenario
        output = invoke_cmd(f'{VISIONAI_EXEC} camera remove-scenario --camera TEST-999 --scenario smoke-and-fire-detection')
        assert 'Successfully removed scenario: smoke-and-fire-detection' in output

        # list scenario
        output = invoke_cmd(f'{VISIONAI_EXEC} camera list-scenario  --camera TEST-999')
        assert "scenarios for camera" in output
        assert 'TEST-999' in output
        assert "'name': 'smoke-and-fire-detection'" not in output

        # remove camera
        output = invoke_cmd(f'{VISIONAI_EXEC} camera remove --name TEST-999')
        assert "Successfully removed camera: TEST-999" in output

        # list scenarios for deleted cam
        output = invoke_cmd(f'{VISIONAI_EXEC} camera list-scenario  --camera TEST-999')
        assert "camera not found: TEST-999" in output

        # list scenario for all
        output = invoke_cmd(f'{VISIONAI_EXEC} camera list-scenarios')
        assert "scenarios for all cameras" in output
        assert "[]" in output


if __name__ == '__main__':
    unittest.main()
