# Importing the numpy library
import numpy as np

# Load data from a .npy file
data = np.load('file.npy')

# Load data from a .npz file
data = np.load('file.npz')
''
# Load data from a pickled file
data = np.load('file.pkl', allow_pickle=True)
