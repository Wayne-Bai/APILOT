import numpy as np

# Load a .npy file
array_from_npy = np.load('filename.npy')

# Load .npz file (which may contain multiple arrays)
with np.load('filename.npz') as data:
    array_from_npz_1 = data['array1']
    array_from_npz_2 = data['array2']

# Load a pickled file (requires allowing pickle)
array_from_pickle = np.load('filename.pkl', allow_pickle=True)
