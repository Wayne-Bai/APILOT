
import yaml

def load_all_yaml_files(directory):
    all_yaml_data = []
    for file in directory:
        with open(file, 'r') as f:
            yaml_data = yaml.safe_load(f)
            all_yaml_data.append(yaml_data)
    return all_yaml_data

# Example usage
directory = ['file1.yaml', 'file2.yaml', 'file3.yaml']
all_yaml_data = load_all_yaml_files(directory)
print(all_yaml_data)
