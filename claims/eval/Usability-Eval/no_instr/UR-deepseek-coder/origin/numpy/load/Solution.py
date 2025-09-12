import numpy as np

# Load a single array from a .npy file
array = np.load('array.npy')

# Load multiple arrays from a .npz file
data = np.load('data.npz')
array1 = data['array1']
array2 = data['array2']

# Load a pickled object from a file
with open('pickled_object.pkl', 'rb') as f:
    pickled_object = np.load(f, allow_pickle=True)
