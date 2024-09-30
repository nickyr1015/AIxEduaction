import json
import os

def get_config():
    with open('./backend/config/config.json', 'r') as file:
        config = json.load(file)
    return config
