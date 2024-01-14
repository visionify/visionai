import json

def print_scenarios():
    with open('scenarios.json') as f:
        scenarios = json.load(f)['scenarios']
        
    cats = {}
    for scenario in scenarios:
        cat = scenario['category_name']
        uuid = scenario['id']
        scen = scenario['title']
        complete = scenario['completed'] if 'completed' in scenario else False
        coming_soon = scenario['coming_soon'] if 'coming_soon' in scenario else False
        # img = scenario['image']
        cats[cat] = {} if cat not in cats else cats[cat]
        cats[cat]['scenario'] = [] if 'scenario' not in cats[cat] else cats[cat]['scenario']
        cats[cat]['scenario'].append((uuid, scen, complete, coming_soon)) if complete or coming_soon else None
        
    for cat in cats:
        print(cat)
        for scenario in cats[cat]['scenario']:
            print(f'\t{scenario}')


def update_uuids():
    import uuid
    
    with open('scenarios.json') as f:
        scenarios = json.load(f)['scenarios']
    
    for scenario in scenarios:
        scenario['id'] = str(uuid.uuid4())
    
    with open('scenarios.json', 'w') as f:
        json.dump({'scenarios': scenarios}, f, indent=2)
        
if __name__ == '__main__':
    print_scenarios()
    # update_uuids()
    