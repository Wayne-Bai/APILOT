import yaml

def load_yaml_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Usage
file_path = 'path_to_your_file.yaml'
loaded_data = load_yaml_file(file_path)
