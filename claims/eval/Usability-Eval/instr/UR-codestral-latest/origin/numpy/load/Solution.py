import numpy as np

# Load arrays from .npy file
arr = np.load('my_array.npy')

# Load array from .npz file
data = np.load('my_data.npz')
arr_from_npz = data['arr']  # 'arr' is the key in the npz file

# Load pickled object from pickled file
import pickle
with open('my_pickled_object.pkl', 'rb') as f:
    pickled_object = pickle.load(f)
