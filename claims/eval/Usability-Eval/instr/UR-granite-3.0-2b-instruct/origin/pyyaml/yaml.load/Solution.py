import yaml

# Load YAML file
with open('file.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Now you can access the data
print(data)
