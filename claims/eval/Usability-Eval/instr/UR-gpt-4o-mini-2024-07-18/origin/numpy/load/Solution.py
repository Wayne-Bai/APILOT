import numpy as np

# Load a single .npy file
array = np.load('file.npy')

# Load multiple arrays from a .npz file
with np.load('file.npz') as data:
    array1 = data['array1_name']
    array2 = data['array2_name']

# Load a pickled object (make sure to use 'rb' mode)
import pickle

with open('file.pkl', 'rb') as f:
    obj = pickle.load(f)
