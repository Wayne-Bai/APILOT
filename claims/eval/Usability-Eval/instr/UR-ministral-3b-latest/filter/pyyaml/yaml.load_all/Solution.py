import pyyaml

def load_all_yaml_files(directory):
    data = {}
    for filename in os.listdir(directory):
        if filename.endswith(".yaml"):
            with open(os.path.join(directory, filename), 'r') as file:
                file_content = file.read()
                parsed_content = pyyaml.safe_load(file_content)
                data[filename] = parsed_content
    return data

# Example usage:
directory = 'path_to_your_yaml_files'
all_yaml_data = load_all_yaml_files(directory)
for filename, content in all_yaml_data.items():
    print(f"File: {filename}")
    for key, value in content.items():
        print(f"  {key}: {value}")
