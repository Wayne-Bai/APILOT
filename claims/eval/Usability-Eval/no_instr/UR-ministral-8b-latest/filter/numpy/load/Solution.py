import numpy as np

# Function to load from .npy file
def load_npy(file_path):
    array = np.load(file_path)
    return array

# Function to load from .npz file
def load_npz(file_path):
    archive = np.load(file_path)
    data = dict((name, archive[name]) for name in archive)
    return data

# Function to load pickled objects from .npz file
def load_pickle_npz(file_path):
    res = np.load(file_path, allow_pickle=True)
    data = dict((name, res[name]) for name in res)
    return data

# Example usage
npy_array = load_npy('example.npy')
print("Numpy array loaded from .npy file:", npy_array)

npz_data = load_npz('example.npz')
print("Data loaded from .npz file:", npz_data)

pickle_data = load_pickle_npz('example_pickle.npz')
print("Pickle objects loaded from .npz file:", pickle_data)
