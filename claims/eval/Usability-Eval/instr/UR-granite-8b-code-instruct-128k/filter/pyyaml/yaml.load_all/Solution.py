import pyyaml
def load_yaml_files(directory_path):
    files = os.listdir(directory_path)
    yaml_files = [file for file in files if file.endswith('.yaml') or file.endswith('.yml')]
    data = {}
    for file in yaml_files:
        with open(os.path.join(directory_path, file), 'r') as f:
            data[file] = pyyaml.load(f, Loader=pyyaml.FullLoader)
    return data
