import numpy as np

def load_data_from_text_file(file_path):
    try:
        # Attempt to load the data from the text file
        data = np.loadtxt(file_path, dtype=str, delimiter=None, comments=None)
        return data
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None
    except np.core._exceptions._ArrayMemoryError as e:
        print(f"An error occurred while loading the file: {e}")
        return None

def load_data_from_text_file_with_gen(file_path):
    try:
        # Attempt to load the data from the text file using a generator
        data = np.fromiter((line.strip().split() for line in open(file_path, 'r')), dtype=float)
        return data
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None
    except np.core._exceptions._ArrayMemoryError as e:
        print(f"An error occurred while loading the file: {e}")
        return None


# Test the functions
file_path = 'example.txt'
print(load_data_from_text_file(file_path))
print(load_data_from_text_file_with_gen(file_path))
