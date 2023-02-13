
import requests
import json
from pathlib import Path

FILE = Path(__file__).resolve()
CONFIGDIR = FILE.parents[0]  # config directory

from config import SCENARIOS_URL, SCENARIOS_OVERRIDE

def main():
    res = requests.get(SCENARIOS_URL)
    scenarios = res.json()
    with open(SCENARIOS_OVERRIDE, 'w') as f:
        json.dump(scenarios, f, indent=4)

    print(f'Scenarios schema {SCENARIOS_URL} downloaded to {SCENARIOS_OVERRIDE}')

if __name__ == '__main__':
    main()
