import numpy as np

# Load arrays or pickled objects from .npy, .npz or pickled files
def load_data(file_path):
    if file_path.endswith('.npy'):
        return np.load(file_path)
    elif file_path.endswith('.npz'):
        return np.load(file_path)
    elif file_path.endswith('.pkl'):
        return np.load(file_path)
    else:
        raise ValueError("Unsupported file format. Only .npy, .npz, and .pkl files are supported.")
