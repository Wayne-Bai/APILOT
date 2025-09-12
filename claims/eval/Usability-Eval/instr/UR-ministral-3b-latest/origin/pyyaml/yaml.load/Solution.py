import yaml

# Assuming 'config.yaml' is the file you want to load
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

print(config)
