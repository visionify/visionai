import unittest
import json, requests
import sys

from pathlib import Path

SCENARIOS_FILE = 'scenarios.json'


class TestScenarioJson(unittest.TestCase):

    def test_scenario_json_file_exist(self):
        my_file = Path(SCENARIOS_FILE)
        assert my_file.is_file()

    def test_scenario_json_file_not_empty(self):
        my_file = Path(SCENARIOS_FILE)
        assert my_file.stat().st_size != 0


    def test_scenario_json_file_has_correct_format(self):
        with open(SCENARIOS_FILE,'r') as f:
            scenarios = json.load(f)
        assert isinstance(scenarios, dict)
        for scenario in scenarios['scenarios']:
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
            
            # assert requests.get(scenario['icon'], stream=True).status_code != 404
            
            assert 'coming_soon' in scenario
            assert 'completed' in scenario
            assert 'tags' in scenario
            assert 'category_name' in scenario
            
            
            

if __name__ == '__main__':
    unittest.main()



