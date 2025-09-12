
import yaml

def load_all_yaml_files(folder_path):
    all_data = []
    # Iterate through all files in the specified folder path
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.yaml'):
            with open(os.path.join(folder_path, file_name), 'r') as file:
                data = yaml.safe_load(file)
                all_data.append(data)
    return all_data
