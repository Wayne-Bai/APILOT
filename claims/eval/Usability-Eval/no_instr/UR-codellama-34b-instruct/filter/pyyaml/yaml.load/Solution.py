
import yaml

with open('example.yaml', 'r') as stream:
    try:
        data = yaml.safe_load(stream)
        print(data)
    except yaml.YAMLError as exc:
        print(exc)
