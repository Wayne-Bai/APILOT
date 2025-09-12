import numpy as np

# Load a .npy file
with open('file.npy', 'rb') as f:
    array = np.load(f)

# Load a .npz file
with open('file.npz', 'rb') as f:
    npz_data = np.load(f)
    data = npz_data['arr_0']

# Load a pickled object
with open('file.pickle', 'rb') as f:
    obj = pickle.load(f)
