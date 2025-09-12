import yaml

def load_yaml_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Usage
file_path = 'file_path/your_file.yaml'
data = load_yaml_file(file_path)
print(data)
