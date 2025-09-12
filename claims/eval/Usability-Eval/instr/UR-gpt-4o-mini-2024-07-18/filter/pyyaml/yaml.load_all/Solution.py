import yaml
import os

def load_yaml_files(directory):
    yaml_data = {}
    for filename in os.listdir(directory):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            with open(os.path.join(directory, filename), 'r') as file:
                try:
                    yaml_content = yaml.safe_load(file)
                    yaml_data[filename] = yaml_content
                except yaml.YAMLError as e:
                    print(f"Error loading {filename}: {e}")
    return yaml_data

# Example usage:
# yaml_files = load_yaml_files('path/to/your/yaml/files')
# print(yaml_files)
