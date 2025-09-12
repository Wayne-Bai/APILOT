from flask import Flask
import json

app = Flask(__name__)

# Load the JSON data into a dictionary
with open('config.json') as f:
    config_data = json.load(f)

# Update the values in the config using the from_mapping() function
app.config.from_mapping(**config_data)
