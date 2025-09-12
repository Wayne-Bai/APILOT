import numpy as np

# Load an array from a .npy file
def load_npy(filepath):
    array = np.load(filepath, allow_pickle=True)
    return array

# Load arrays from a .npz file
def load_npz(filepath):
    data = np.load(filepath)
    arrays = data.files
    loaded_arrays = {name: data[name] for name in arrays}
    return loaded_arrays

# Load a pickled object from a .pkl file
def load_pickle(filepath):
    with open(filepath, 'rb') as file:
        pickled_obj = np.load(file, allow_pickle=True)

    return pickled_obj

# Example usage
if __name__ == "__main__":
    # Loading from a .npy file
    npy_array = load_npy('example.npy')
    print("Loaded .npy array:", npy_array)

    # Loading from a .npz file
    npz_data = load_npz('example.npz')
    for key, array in npz_data.items():
        print(f"Loaded .npz array: {key}")
        print(array)

    # Loading from a .pkl file
    pickle_obj = load_pickle('example.pkl')
    print("Loaded .pkl object:", pickle_obj)
