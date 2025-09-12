import numpy as np

# Load .npy file
arr = np.load('file.npy')

# Load .npz file
data = np.load('file.npz')

# Load pickled file
with open('file.pkl', 'rb') as f:
    data = pickle.load(f)
