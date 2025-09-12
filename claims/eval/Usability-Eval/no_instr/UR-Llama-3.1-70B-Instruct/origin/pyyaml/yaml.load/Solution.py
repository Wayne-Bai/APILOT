# Import the yaml module from the pyyaml library
import yaml

def load_yaml_file(file_path):
    """
    Load a YAML file and return the data as a Python dictionary.

    Args:
        file_path (str): The path to the YAML file to load.

    Returns:
        dict: The data from the YAML file as a Python dictionary.
    """
    try:
        # Open the YAML file in read mode
        with open(file_path, 'r') as file:
            # Use the safe_load function to parse the YAML data
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None

# Example usage:
file_path = 'example.yaml'
data = load_yaml_file(file_path)

if data is not None:
    print(data)
