import yaml

# Load YAML file using safe_load from PyYAML
def load_yaml_file(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    return data
