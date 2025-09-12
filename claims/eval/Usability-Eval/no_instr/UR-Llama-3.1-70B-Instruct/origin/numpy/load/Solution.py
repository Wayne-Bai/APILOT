import numpy as np

# Load arrays from.npy file
def load_npy_file(file_path):
    try:
        data = np.load(file_path, allow_pickle=False)
        print("Loaded array from.npy file:")
        print(data)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred: ", str(e))

# Load arrays or pickled objects from.npz file
def load_npz_file(file_path):
    try:
        with np.load(file_path, allow_pickle=False) as data:
            print("Loaded arrays from.npz file:")
            for key in data.files:
                print(f"{key}: {data[key]}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred: ", str(e))

# Load pickled objects from file
def load_pickled_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            data = np.load(f, allow_pickle=True)
            print("Loaded pickled object from file:")
            print(data)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred: ", str(e))

# Test the functions
load_npy_file('example.npy')
load_npz_file('example.npz')
load_pickled_file('example.pkl')
