import numpy as np

# Load arrays from .npy file
arr = np.load('array.npy')

# Load arrays from .npz file
data = np.load('file.npz')
arr1 = data['arr1']
arr2 = data['arr2']

# Load pickled objects from .pkl file
import pickle
with open('file.pkl', 'rb') as f:
    obj = pickle.load(f)

# Load pickled objects from .pkl.gz file
import gzip
with gzip.open('file.pkl.gz', 'rb') as f:
    obj = pickle.load(f)
