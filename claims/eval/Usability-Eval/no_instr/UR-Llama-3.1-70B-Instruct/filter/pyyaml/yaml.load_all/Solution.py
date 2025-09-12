import yaml
import os

def load_yaml_files(directory):
    """
    Loads all YAML files in a given directory.

    Args:
        directory (str): Path to the directory containing YAML files.

    Returns:
        list: A list of dictionaries, where each dictionary represents a loaded YAML file.
    """
    yaml_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r') as file:
                    yaml_files.append(yaml.safe_load(file))
            except yaml.YAMLError as e:
                print(f"Failed to load YAML file: {filename}. Error: {e}")
    return yaml_files

# Example usage:
directory = 'path/to/yaml/files'
loaded_yamls = load_yaml_files(directory)
for i, yaml_data in enumerate(loaded_yamls):
    print(f"Loaded YAML file {i+1}:")
    print(yaml_data)
    print()
