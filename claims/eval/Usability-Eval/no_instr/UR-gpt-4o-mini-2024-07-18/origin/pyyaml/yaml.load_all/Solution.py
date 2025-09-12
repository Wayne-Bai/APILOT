import yaml
import os

def load_yaml_files(directory):
    yaml_data = {}
    for filename in os.listdir(directory):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                yaml_data[filename] = yaml.safe_load(file)
    return yaml_data

# Example usage
directory_path = 'path/to/your/yaml/files'  # Replace with your directory path
loaded_data = load_yaml_files(directory_path)
print(loaded_data)
