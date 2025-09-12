
import yaml

# Open the YAML file for reading
with open('example.yaml', 'r') as f:
    # Load the YAML file into a dictionary
    data = yaml.load(f)

print(data)
