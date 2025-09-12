import os
import yaml

def load_yaml_file(file_path):
    """
    Load yaml file from the specified file path.

    Args:
        file_path (str): The path to the yaml file to be loaded.

    Returns:
        dict: The loaded yaml data.
    """
    try:
        with open(file_path, 'r') as yaml_file:
            return yaml.safe_load(yaml_file)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return {}
    except yaml.YAMLError as e:
        print(f"Error loading file {file_path}: {e}")
        return {}

def load_all_yaml_files(directory_path):
    """
    Load all yaml files from the specified directory.

    Args:
        directory_path (str): The path to the directory containing yaml files.

    Returns:
        dict: A dictionary containing the loaded yaml data for each file.
    """
    yaml_data = {}
    for filename in os.listdir(directory_path):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            file_path = os.path.join(directory_path, filename)
            yaml_data[filename] = load_yaml_file(file_path)
    return yaml_data

# Example usage:
directory_path = '/path/to/yaml/files'
loaded_data = load_all_yaml_files(directory_path)
print(loaded_data)
