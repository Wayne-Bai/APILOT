import yaml

# List of YAML files to load
yaml_files = ['file1.yaml', 'file2.yaml', 'file3.yaml']

# Load each YAML file and print its contents
for file in yaml_files:
    with open(file, 'r') as f:
        contents = yaml.safe_load(f)
        print(contents)
