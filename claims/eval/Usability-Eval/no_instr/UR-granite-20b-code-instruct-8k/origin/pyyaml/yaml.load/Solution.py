import yaml

# Load the YAML file
with open("example.yaml", "r") as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# Access the data
print(data)
