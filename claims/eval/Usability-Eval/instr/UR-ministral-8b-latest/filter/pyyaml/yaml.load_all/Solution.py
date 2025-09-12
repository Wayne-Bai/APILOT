import yaml

def load_yaml_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

if __name__ == "__main__":
    yaml_files = ["file1.yaml", "file2.yaml", "file3.yaml"]  # List your YAML files here
    for file in yaml_files:
        data = load_yaml_file(file)
        print(f"Data from {file}:\n{data}\n")
