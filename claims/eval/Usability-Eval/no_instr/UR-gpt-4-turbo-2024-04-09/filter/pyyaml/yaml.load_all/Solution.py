import yaml

# Ensure to use the safe_load function to avoid any security risks
with open('yourfile.yaml', 'r') as file:
    data = yaml.safe_load(file)

print(data)
