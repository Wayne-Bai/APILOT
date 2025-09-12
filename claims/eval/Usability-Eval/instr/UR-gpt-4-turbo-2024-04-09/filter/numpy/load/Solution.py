import numpy as np

# Loading a single array from a .npy file
npy_file_path = 'path_to_your_file.npy'
data_from_npy = np.load(npy_file_path)
print("Data loaded from .npy file:", data_from_npy)

# Loading multiple arrays from a .npz file
npz_file_path = 'path_to_your_file.npz'
data_from_npz = np.load(npz_file_path)
# npz files contain multiple arrays, each identified by a keyword.
# Assuming 'array1' and 'array2' are keywords in the .npz file.
array1 = data_from_npz['array1']
array2 = data_from_npz['array2']
data_from_npz.close()  # Close the file after extraction
print("Array 1 from .npz file:", array1)
print("Array 2 from .npz file:", array2)

# Loading a pickled object
import pickle

pickle_file_path = 'path_to_your_pickle_file.pkl'
with open(pickle_file_path, 'rb') as file:
    pickled_data = pickle.load(file)
print("Data loaded from pickle file:", pickled_data)
