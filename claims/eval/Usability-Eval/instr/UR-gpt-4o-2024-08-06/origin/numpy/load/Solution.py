import numpy as np

# Load array from a .npy file
array_from_npy = np.load('example.npy')

# Load arrays from a .npz file
arrays_from_npz = np.load('example.npz')
array_1 = arrays_from_npz['arr_1']   # Assuming there is an array named 'arr_1' in the .npz file
array_2 = arrays_from_npz['arr_2']   # Assuming there is an array named 'arr_2' in the .npz file

# Load a pickled object from a file
with open('example.pkl', 'rb') as file:
    pickled_object = np.load(file, allow_pickle=True)

# Ensure you close the .npz file with context management or manual closure
arrays_from_npz.close()
