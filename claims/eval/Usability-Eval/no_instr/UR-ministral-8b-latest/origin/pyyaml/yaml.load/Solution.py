import yaml

# Function to load YAML file
def load_yaml_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Example usage
if __name__ == "__main__":
    file_path = 'path/to/your/file.yaml'
    yaml_data = load_yaml_file(file_path)
    print(yaml_data)
