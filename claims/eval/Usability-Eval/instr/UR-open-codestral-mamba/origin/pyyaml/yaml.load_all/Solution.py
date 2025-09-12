import yaml

def load_yaml_file(file_name):
    with open(file_name, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Example usage:
# data = load_yaml_file('your_file.yaml')
# print(data)
