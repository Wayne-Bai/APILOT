import numpy as np

# Load .npy file
data_npy = np.load('file.npy')

# Load .npz file
data_npz = np.load('file.npz')
print(data_npz.files)  # Print all files in the archive
arr_1 = data_npz['arr_1']  # Extract array 'arr_1' from the archive

# Load pickle file
import pickle
with open('file.pkl', 'rb') as f:
    data_pkl = pickle.load(f)
