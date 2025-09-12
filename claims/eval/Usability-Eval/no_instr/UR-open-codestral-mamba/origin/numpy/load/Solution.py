import numpy as np

# Load array from .npy file
array_from_npy = np.load('file.npy')

# Load array from .npz file
npz_file = np.load('file.npz')
for key in npz_file.files:
    array_from_npz = npz_file[key]

# Load pickled object from .pkl or .pickle file
import pickle
with open('file.pkl', 'rb') as f:
    object_from_pkl = pickle.load(f)
with open('file.pickle', 'rb') as f:
    object_from_pickle = pickle.load(f)
