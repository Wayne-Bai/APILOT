
import numpy as np

# Load arrays from .npy file
data = np.load('filename.npy')

# Load arrays from .npz file
with np.load('filename.npz') as data:
    array1 = data['array1']
    array2 = data['array2']

# Load pickled objects from file
with open('filename.pkl', 'rb') as f:
    obj = pickle.load(f)
