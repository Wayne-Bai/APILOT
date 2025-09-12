# Import pyyaml library
import yaml

# Define a function to load YAML file
def load_yaml_file(file_path):
    """
    This function loads a YAML file and returns the contents as a Python dictionary.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        dict: The contents of the YAML file as a Python dictionary.
    """
    try:
        # Open the YAML file in read mode
        with open(file_path, 'r') as file:
            # Load the YAML file contents into a Python dictionary
            yaml_contents = yaml.safe_load(file)
            return yaml_contents
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Specify the path to your YAML file
    yaml_file_path = 'example.yaml'
    
    # Load the YAML file
    yaml_contents = load_yaml_file(yaml_file_path)
    
    # Print the loaded YAML contents
    print(yaml_contents)
