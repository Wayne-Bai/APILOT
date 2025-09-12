import yaml

# Load the YAML file
with open('example.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Print the data
print(data)
