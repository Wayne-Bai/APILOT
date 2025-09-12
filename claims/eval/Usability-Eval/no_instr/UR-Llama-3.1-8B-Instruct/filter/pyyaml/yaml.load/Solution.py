# Import the pyyaml library
import yaml

def load_yaml_file(file_path):
    """
    Loads a YAML file and returns the contents as a dictionary.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        dict: The contents of the YAML file as a dictionary.
    """
    try:
        # Open the YAML file in read mode
        with open(file_path, 'r') as file:
            # Use yaml.safe_load() to load the YAML file
            # This is the recommended way to load YAML files in Python
            contents = yaml.safe_load(file)
            return contents
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None

# Example usage
if __name__ == "__main__":
    file_path = 'example.yaml'  # Replace with your YAML file path
    data = load_yaml_file(file_path)
    if data is not None:
        print(data)
