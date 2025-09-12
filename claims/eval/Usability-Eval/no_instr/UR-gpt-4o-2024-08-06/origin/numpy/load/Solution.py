import numpy as np

# To load a single array from a .npy file
array_from_npy = np.load('your_array_file.npy')

# To load multiple arrays from a .npz file
arrays_from_npz = np.load('your_arrays_file.npz')
for array_name in arrays_from_npz:
    print(f"{array_name}: {arrays_from_npz[array_name]}")

# To load a pickled object
# First, ensure the file was saved using np.save or np.savez with allow_pickle=True
object_from_pickle = np.load('your_pickle_file.npy', allow_pickle=True)
print(object_from_pickle)
