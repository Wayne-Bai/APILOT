import numpy as np

# Load a single array from a .npy file
array = np.load('filename.npy')

# Load multiple arrays from a .npz file
data = np.load('filename.npz')
array1 = data['array1']  # Replace 'array1' with the actual key name
array2 = data['array2']  # Replace 'array2' with the actual key name

# Load a pickled object from a .pkl file
import pickle

with open('filename.pkl', 'rb') as f:
    pickled_object = pickle.load(f)
