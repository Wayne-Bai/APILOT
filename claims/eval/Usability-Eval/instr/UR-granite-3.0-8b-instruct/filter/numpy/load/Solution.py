import numpy as np

# Load .npy file
array = np.load('file.npy')

# Load .npz file
data = np.load('file.npz')

# Load pickled object
with open('file.pkl', 'rb') as f:
    data = pickle.load(f)
