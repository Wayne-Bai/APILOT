import numpy as np

# Load a .npy file
data = np.load('file.npy')

# Load a .npz file
loaded_data = np.load('file.npz')

# Access data from the .npz file
data1 = loaded_data['arr_0']
data2 = loaded_data['arr_1']

# Load a pickled object
with open('file.pkl', 'rb') as f:
    loaded_object = pickle.load(f)
