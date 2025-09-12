import yaml

def load_yaml_file(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Example usage:
# Replace 'yourfile.yaml' with your actual YAML file path
yaml_data = load_yaml_file('yourfile.yaml')
print(yaml_data)
