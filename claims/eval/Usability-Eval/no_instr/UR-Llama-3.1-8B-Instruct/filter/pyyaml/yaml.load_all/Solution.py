# Import the yaml module from python, which provides a lean and efficient 
# YAML parser and emitter.
import yaml

# Initialize an empty dictionary to store data from each yaml file
all_data = {}

# Define the function to load data from each yaml file
def load_yaml_files():
    # Specify the path to the directory containing yaml files
    yaml_dir = 'path_to_your_yaml_files'

    # Iterate over each file in the specified directory
    for filename in next(os.walk(yaml_dir))[2]:
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            with open(os.path.join(yaml_dir, filename), 'r') as f:
                try:
                    # Attempt to load the yaml file
                    data = yaml.safe_load(f)
                    # If the data is a dictionary, update all_data
                    if data is not None and isinstance(data, dict):
                        all_data.update(data)
                    # If the data is a list, append it to all_data
                    elif data is not None and isinstance(data, list):
                        if 'data' not in all_data:
                            all_data['data'] = []
                        all_data['data'].extend(data)
                    # If the data is neither a dictionary nor a list, append it to all_data as a key-value pair
                    else:
                        if 'other_data' not in all_data:
                            all_data['other_data'] = {}
                        all_data['other_data'][filename] = data
                except yaml.YAMLError as e:
                    print(f"Error loading {filename}: {e}")

# Use the load_yaml_files function to load all yaml files
load_yaml_files()

# Print the loaded data
print(all_data)

