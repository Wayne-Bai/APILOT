import numpy as np

# Load a .npy file
data = np.load('file.npy')

# Load a .npz file
data = np.load('file.npz')

# Load a pickled file
with open('file.pkl', 'rb') as f:
    data = pickle.load(f)
