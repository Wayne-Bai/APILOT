
import numpy as np

# Load a .npy file
arr = np.load('file.npy')

# Load a .npz file
data = np.load('file.npz')
arr1 = data['arr1']
arr2 = data['arr2']

# Load a pickled file
with open('file.pkl', 'rb') as f:
    obj = pickle.load(f)
