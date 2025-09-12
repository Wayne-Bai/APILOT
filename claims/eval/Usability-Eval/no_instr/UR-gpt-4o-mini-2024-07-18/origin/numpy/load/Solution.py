import numpy as np

# Function to load arrays from .npy, .npz or pickled files
def load_array(file_path):
    if file_path.endswith('.npy'):
        return np.load(file_path)
    elif file_path.endswith('.npz'):
        with np.load(file_path) as data:
            return {key: data[key] for key in data}
    elif file_path.endswith('.pkl') or file_path.endswith('.pickle'):
        import pickle
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    else:
        raise ValueError("Unsupported file format. Please provide a .npy, .npz, or .pkl file.")
