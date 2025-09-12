
import numpy as np

# Load .npy file
arr = np.load('array.npy')

# Load .npz file
data = np.load('data.npz')
arr1 = data['arr1']
arr2 = data['arr2']

# Load pickled file
import pickle
with open('pickle_file.pkl', 'rb') as f:
    obj = pickle.load(f)
