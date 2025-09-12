
import yaml

with open("config.yaml", "r") as f:
    data = yaml.load(f)

print(data)
