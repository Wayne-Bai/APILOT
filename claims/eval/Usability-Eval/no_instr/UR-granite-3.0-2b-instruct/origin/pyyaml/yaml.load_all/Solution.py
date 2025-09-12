import yaml

# Load all yaml files in a directory
for filename in os.listdir("path/to/yaml/files"):
    if filename.endswith(".yaml"):
        with open(os.path.join("path/to/yaml/files", filename), "r") as file:
            data = yaml.safe_load(file)
            # Process the data as needed
