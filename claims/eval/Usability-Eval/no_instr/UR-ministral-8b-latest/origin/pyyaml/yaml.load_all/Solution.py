import yaml

def load_all_yaml_files(directory):
    yaml_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                yaml_files.append(yaml.safe_load(file))
    return yaml_files

# Example usage
directory_path = '/path/to/yaml/files'
yaml_data = load_all_yaml_files(directory_path)
for data in yaml_data:
    print(data)
