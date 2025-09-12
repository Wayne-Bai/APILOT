import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

# Use the function to load a yaml file
#print(load_yaml('your_file.yaml'))
