import json

def load_api_keys():
    with open('keys.json', 'r') as f:
        config = json.load(f)
    return config['API_KEY'], config['SECRET_KEY']