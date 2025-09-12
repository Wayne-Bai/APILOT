import yaml

# Load the contents of the YAML file
def load_yaml_file(file_path):
    with open(file_path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

# Usage
yaml_data = load_yaml_file('path_to_your_yaml_file.yaml')
