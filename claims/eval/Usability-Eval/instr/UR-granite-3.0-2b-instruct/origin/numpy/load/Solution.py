import numpy as np

# Load arrays or pickled objects from .npy, .npz or pickled files
def load_data(file_path):
    if file_path.endswith('.npy'):
        return np.load(file_path)
    elif file_path.endswith('.npz'):
        return np.load(file_path, allow_pickle=True)
    elif file_path.endswith('.pkl'):
        return np.load(file_path, allow_pickle=True)
    else:
        raise ValueError("Unsupported file format. Please provide a .npy, .npz or .pkl file.")
