import yaml

def load_yaml_files(directory):
    """
    Loads all YAML files from a given directory.

    Args:
        directory (str): Path to the directory containing the YAML files.

    Returns:
        dict: A dictionary containing all the YAML files' data.
    """
    data = {}
    for file in yaml.safe_load_all(open(directory, 'r')):
        data.update(file)
    return data


def load_yaml_files_recursive(directory):
    """
    Loads all YAML files from a given directory and its subdirectories.

    Args:
        directory (str): Path to the directory containing the YAML files.

    Returns:
        dict: A dictionary containing all the YAML files' data.
    """
    data = {}
    for dirpath, _, filenames in os.walk(directory):
        for file in filenames:
            if file.endswith(".yaml") or file.endswith(".yml"):
                filepath = os.path.join(dirpath, file)
                with open(filepath, 'r') as f:
                    data.update(yaml.safe_load(f))
    return data


import os

# Example usage:
directory = '/path/to/your/directory'
data = load_yaml_files_recursive(directory)
print(data)
