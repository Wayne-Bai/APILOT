import numpy as np

# To load a .npy file
npy_array = np.load('filename.npy')

# To load a .npz file
npz_data = np.load('filename.npz')
# If there's a need to access the arrays in the npz file:
# accessed_array = npz_data['array_name']

# To load a pickled file using numpy:
with open('filename.pkl', 'rb') as f:
    pickled_data = np.load(f, allow_pickle=True)
