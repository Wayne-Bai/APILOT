import yaml

# Load all yaml files in a directory
import os

for filename in os.listdir("path/to/your/yaml/files"):
    if filename.endswith(".yaml"):
        with open(os.path.join("path/to/your/yaml/files", filename), "r") as file:
            data = yaml.safe_load(file)
        print(data)
