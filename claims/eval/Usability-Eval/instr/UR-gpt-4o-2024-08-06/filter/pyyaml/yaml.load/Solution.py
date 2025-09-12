import yaml

# Load a YAML file
def load_yaml_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Example usage
# yaml_data = load_yaml_file('example.yaml')
# print(yaml_data)
