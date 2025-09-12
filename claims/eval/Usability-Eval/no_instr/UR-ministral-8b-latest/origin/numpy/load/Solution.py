import numpy as np

def load_array(filename):
    if filename.endswith('.npy'):
        return np.load(filename)
    elif filename.endswith('.npz'):
        with np.load(filename) as data:
            return data['file_name']  # Replace 'file_name' with the actual key name
    elif filename.endswith('.pkl') or filename.endswith('.pickle'):
        return np.load(filename)  # Assuming pickled objects are also numpy arrays
    else:
        raise ValueError(f"Unsupported file format: {filename}")

# Usage
# array = load_array('path/to/your/file.npy')
