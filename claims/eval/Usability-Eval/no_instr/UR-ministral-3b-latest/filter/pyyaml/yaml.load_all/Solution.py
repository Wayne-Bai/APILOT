import yaml

def load_yaml_files(directory):
    files = []
    for filename in os.listdir(directory):
        if filename.endswith(".yaml"):
            files.append(filename)
    return files

def load_yaml_contents(directory):
    contents = {}
    for file in os.listdir(directory):
        if file.endswith(".yaml"):
            with open(os.path.join(directory, file), 'r') as stream:
                try:
                    contents[file] = yaml.load(stream, Loader=yaml.SafeLoader)
                except yaml.YAMLError as e:
                    print(f"Error parsing {file}: {e}")
    return contents

# Usage
directory = "/path/to/your/directory"
files = load_yaml_files(directory)
print(files)

contents = load_yaml_contents(directory)
print(contents)
