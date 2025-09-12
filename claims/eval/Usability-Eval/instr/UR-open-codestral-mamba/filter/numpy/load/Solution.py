import numpy as np

# Load .npy files
npy_file = np.load('filename.npy')

# Load .npz files
npz_file = np.load('filename.npz')

# Load pickled files
import pickle
with open('filename.pickle', 'rb') as f:
    pickle_file = pickle.load(f)
