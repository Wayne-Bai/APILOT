import numpy as np

# Load an array from a .npy file
array_from_npy = np.load('filename.npy')

# Load an object from a pickled file
object_from_pickle = np.load('filename.pickle', allow_pickle=True)
