import yaml

def load_yaml_files(file_paths):
    data = {}
    for path in file_paths:
        with open(path, 'r') as file:
            data.update(yaml.safe_load(file))
    return data
