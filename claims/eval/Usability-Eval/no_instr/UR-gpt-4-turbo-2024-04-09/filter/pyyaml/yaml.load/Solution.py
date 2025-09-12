import yaml

# Load YAML file safely
def load_yaml_file(filepath):
    with open(filepath, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Example usage
yaml_data = load_yaml_file('example.yaml')
print(yaml_data)
