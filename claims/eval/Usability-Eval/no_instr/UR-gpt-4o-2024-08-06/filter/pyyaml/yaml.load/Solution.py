import yaml

# Load YAML file
def load_yaml_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Example usage
file_path = 'example.yaml'
yaml_content = load_yaml_file(file_path)
print(yaml_content)
