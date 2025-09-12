import numpy as np

# Loading a .npy file
array_from_npy = np.load('file.npy')

# Loading a .npz file
array_from_npz = np.load('file.npz')['arr_0']  # if the array was saved by np.savez('file.npz', arr_0=array)

# Loading a pickled file
array_from_pickle = np.load('file.pickle', allow_pickle=True)
