import yaml
import os

def load_yaml_files(directory):
    yaml_data = {}
    for filename in os.listdir(directory):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                try:
                    data = yaml.safe_load(file)
                    yaml_data[filename] = data
                except yaml.YAMLError as e:
                    print(f"Error loading {filename}: {e}")
    return yaml_data

# Example usage
# directory_path = 'path/to/your/yaml/directory'
# all_yaml_data = load_yaml_files(directory_path)
# print(all_yaml_data)
