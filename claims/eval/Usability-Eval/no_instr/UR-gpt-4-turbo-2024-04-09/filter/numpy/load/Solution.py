import numpy as np

# Function to load a .npy file
def load_npy_file(filepath):
    return np.load(filepath, allow_pickle=True)

# Function to load a .npz file
def load_npz_file(filepath):
    with np.load(filepath, allow_pickle=True) as data:
        return {file: data[file] for file in data}

# Function to load a pickled file
def load_pickled_file(filepath):
    import pickle
    with open(filepath, 'rb') as file:
        return pickle.load(file)

# Example usage
npy_data = load_npy_file('example.npy')
npz_data = load_npz_file('example.npz')
pickled_data = load_pickled_file('example.pkl')

print("Loaded .npy data:", npy_data)
print("Loaded .npz data:", npz_data)
print("Loaded pickled data:", pickled_data)
