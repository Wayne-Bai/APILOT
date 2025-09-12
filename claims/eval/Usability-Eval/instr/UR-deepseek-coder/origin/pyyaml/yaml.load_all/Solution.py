import yaml

def load_yaml_files(file_paths):
    loaded_data = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            loaded_data.append(data)
    return loaded_data

# Example usage:
# file_paths = ['file1.yaml', 'file2.yaml']
# loaded_data = load_yaml_files(file_paths)
# print(loaded_data)
