import numpy as np

# Load arrays from.npy file
def load_npy(file_path):
    """
    Load arrays from.npy file.

    Parameters:
    file_path (str): Path to the.npy file.

    Returns:
    array: Loaded array from the.npy file.
    """
    try:
        array = np.load(file_path, allow_pickle=True)
        return array
    except Exception as e:
        print(f"Error loading.npy file: {e}")

# Load pickled objects from.npz file
def load_npz(file_path):
    """
    Load pickled objects from.npz file.

    Parameters:
    file_path (str): Path to the.npz file.

    Returns:
    dict: Loaded pickled objects from the.npz file.
    """
    try:
        loaded_npz = np.load(file_path, allow_pickle=True)
        return loaded_npz
    except Exception as e:
        print(f"Error loading.npz file: {e}")

# Load pickled objects from.pkl or.pickeled files
import pickle

def load_pickle(file_path):
    """
    Load pickled objects from.pkl or.pickled files.

    Parameters:
    file_path (str): Path to the.pkl or.pickled file.

    Returns:
    object: Loaded pickled object from the.pkl or.pickled file.
    """
    try:
        with open(file_path, 'rb') as file:
            object = pickle.load(file)
            return object
    except Exception as e:
        print(f"Error loading.pkl or.pickled file: {e}")

# Example usage
npy_file_path = 'data.npy'
npz_file_path = 'data.npz'
pickle_file_path = 'data.pkl'

npy_array = load_npy(npy_file_path)
npz_object = load_npz(npz_file_path)
pickle_object = load_pickle(pickle_file_path)

print("Loaded NPY array:", npy_array)
print("Loaded NPZ object:", npz_object)
print("Loaded PICKLE object:", pickle_object)
