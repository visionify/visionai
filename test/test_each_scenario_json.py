import unittest
import json, requests
import os
from pathlib import Path
from parameterized import parameterized

SCENARIO_DETAILS_FOLDER = "each_scenario_details/"





class TestScenarioJson(unittest.TestCase):
    @parameterized.expand([(file,) for file in os.listdir(SCENARIO_DETAILS_FOLDER) if file.endswith('.json')])
    def test_scenario_json_file_exist(self, scenario_file):
        SCENARIOS_FILE = os.path.join(SCENARIO_DETAILS_FOLDER, scenario_file)
        my_file = Path(SCENARIOS_FILE)

    @parameterized.expand([(file,) for file in os.listdir(SCENARIO_DETAILS_FOLDER) if file.endswith('.json')])
    def test_scenario_json_file_exist(self, scenario_file):
        SCENARIOS_FILE = os.path.join(SCENARIO_DETAILS_FOLDER, scenario_file)
        my_file = Path(SCENARIOS_FILE)
        assert my_file.is_file()

    @parameterized.expand([(file,) for file in os.listdir(SCENARIO_DETAILS_FOLDER) if file.endswith('.json')])
    def test_scenario_json_file_not_empty(self,scenario_file):
        SCENARIOS_FILE = os.path.join(SCENARIO_DETAILS_FOLDER, scenario_file)
        my_file = Path(SCENARIOS_FILE)
        assert my_file.stat().st_size != 0

    @parameterized.expand([(file,) for file in os.listdir(SCENARIO_DETAILS_FOLDER) if file.endswith('.json')])
    def test_scenario_json_file_has_correct_format(self, scenario_file):
        SCENARIOS_FILE = os.path.join(SCENARIO_DETAILS_FOLDER, scenario_file)
        with open(SCENARIOS_FILE,'r') as f:
            scenario = json.load(f)
        assert isinstance(scenario, dict)
            
        assert 'id' in scenario
        assert len(scenario['id']) > 0

        assert 'title' in scenario
        assert len(scenario['title']) > 0
        
        assert 'name' in scenario
        assert len(scenario['name']) > 0

        assert 'version' in scenario
        assert len(scenario['version']) > 0
        
        assert 'tagline' in scenario
        assert len(scenario['tagline']) > 0
        
        assert 'overview' in scenario
        assert len(scenario['tagline']) > 0
        
        assert isinstance(scenario['video_clips'], list)
        
        assert 'coming_soon' in scenario
        assert 'completed' in scenario
        

        # assert requests.get(scenario['icon'], stream=True).status_code != 404
        

        if(bool(scenario['models']['latest'])):
            assert requests.get(scenario['models']['latest']['model_url'], stream=True).status_code != 404

        assert isinstance(scenario['models'], dict)
        assert isinstance(scenario['models']['latest'], dict)
        assert isinstance(scenario['models']['other'], list)

        assert 'version' in scenario['models']['latest']
        assert len(scenario['models']['latest']['version']) > 0

        assert 'name' in scenario['models']['latest']
        assert len(scenario['models']['latest']['name']) > 0

        assert 'precision' in scenario['models']['latest']
        assert 'recall' in scenario['models']['latest']
        assert 'f1' in scenario['models']['latest']
        assert 'datasetSize' in scenario['models']['latest']

        assert isinstance(scenario['events'], dict)
        assert len(scenario['events']) > 0
        


if __name__ == '__main__':
    unittest.main()