
import yaml

# Load the YAML file
with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)

# Extract the values for the specified keys
app_name = config['application']['name']
app_version = config['application']['version']

print(app_name, app_version)
