import yaml

# Load YAML file
with open('example.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Print the loaded data
print(data)
