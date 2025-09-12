
import numpy as np

# Load an array from a .npy file
array_from_npy = np.load('file.npy')

# Load an array from a .npz file
data = np.load('file.npz')
array_from_npz = data['array']

# Load pickled objects from a pickle file
with open('file.pkl', 'rb') as f:
    pickled_obj = pickle.load(f)
