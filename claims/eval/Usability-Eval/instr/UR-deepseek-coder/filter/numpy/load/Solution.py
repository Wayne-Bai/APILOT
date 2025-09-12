import numpy as np

# Load a single array from a .npy file
array = np.load('filename.npy')

# Load multiple arrays from a .npz file
data = np.load('filename.npz')
array1 = data['array1']
array2 = data['array2']

# Load a pickled object from a file
with open('filename.pkl', 'rb') as f:
    pickled_object = np.load(f, allow_pickle=True)
