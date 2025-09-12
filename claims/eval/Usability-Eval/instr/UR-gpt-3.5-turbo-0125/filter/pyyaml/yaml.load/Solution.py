
import yaml

def load_yaml_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    
    return data

# Example usage
file_path = 'example.yaml'
data = load_yaml_file(file_path)
print(data)
