import numpy as np

# Load a single array from a .npy file
array = np.load('filename.npy')

# Load multiple arrays from a .npz file
data = np.load('filename.npz')
array1 = data['array1_name']
array2 = data['array2_name']

# Load a pickled object from a .pkl file
import pickle

with open('filename.pkl', 'rb') as file:
    obj = pickle.load(file)
