import numpy as np
import pickle

# Load npy file
def load_npy(file_path):
    """Load numpy array from.npy file"""
    try:
        return np.load(file_path)
    except Exception as e:
        print(f"Error loading npy file: {e}")

# Load npz file
def load_npz(file_path):
    """Load numpy arrays from.npz file"""
    try:
        return np.load(file_path)
    except Exception as e:
        print(f"Error loading npz file: {e}")

# Load pickled file
def load_pickle(file_path):
    """Load pickled object from.pkl file"""
    try:
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        print(f"Error loading pickled file: {e}")

# Example usage:
npy_file_path = 'example.npy'
npz_file_path = 'example.npz'
pickle_file_path = 'example.pkl'

npy_array = load_npy(npy_file_path)
npz_arrays = load_npz(npz_file_path)
pickled_object = load_pickle(pickle_file_path)

print("Loaded npy array:")
print(npy_array)
print("\nLoaded npz arrays:")
print(npz_arrays)
print("\nLoaded pickled object:")
print(pickled_object)
