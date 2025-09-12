import yaml

def load_all_yaml_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            with open(os.path.join(directory, filename), 'r') as file:
                try:
                    data = yaml.safe_load(file)
                    # Process the data as needed
                    print(data)
                except yaml.YAMLError as exc:
                    print(exc)

# Replace 'your_directory' with the path to your directory
load_all_yaml_files('your_directory')
