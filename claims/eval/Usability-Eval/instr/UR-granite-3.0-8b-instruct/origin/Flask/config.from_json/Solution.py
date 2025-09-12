from flask import Flask
import json

app = Flask(__name__)

# Load config from JSON file
with open('config.json') as f:
    config = json.load(f)

# Update config values
config['new_key'] = 'new_value'

# Save updated config to JSON file
with open('config.json', 'w') as f:
    json.dump(config, f)
