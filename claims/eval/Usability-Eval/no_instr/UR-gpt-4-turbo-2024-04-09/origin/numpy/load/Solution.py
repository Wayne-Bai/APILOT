import numpy as np

def load_data(file_path):
    if file_path.endswith('.npy'):
        data = np.load(file_path, allow_pickle=True)
        return data
    elif file_path.endswith('.npz'):
        data = np.load(file_path, allow_pickle=True)
        return {file: data[file] for file in data.files}
    else:
        raise ValueError("Unsupported file format. Supported formats: .npy, .npz")
