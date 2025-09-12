
import yaml

# Define the file path
file_path = 'data.yaml'

# Load the YAML file
with open(file_path, 'r') as file:
    data = yaml.safe_load(file)

print(data)
