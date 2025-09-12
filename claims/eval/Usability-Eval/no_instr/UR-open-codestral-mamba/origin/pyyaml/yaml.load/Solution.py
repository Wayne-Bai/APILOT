import yaml

# Path to the YAML file
yaml_file_path = "/path/to/your_file.yaml"

# Load the YAML file
with open(yaml_file_path, 'r') as file:
    data = yaml.safe_load(file)

print(data)
