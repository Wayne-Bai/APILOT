import numpy as np

def load_data_from_text_file(file_path):
    try:
        data = np.loadtxt(file_path)
        return data
    except FileNotFoundError:
        print(f"The file {file_path} does not exist")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
