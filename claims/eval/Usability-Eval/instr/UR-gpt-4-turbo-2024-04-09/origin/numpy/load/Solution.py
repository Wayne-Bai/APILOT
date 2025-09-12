import numpy as np

def load_data(file_path):
    # Determine the file extension and act accordingly
    file_extension = file_path.split('.')[-1]
    
    if file_extension == 'npy':
        # Load a single array from a .npy file
        data = np.load(file_path, allow_pickle=True)
        return data
    elif file_extension == 'npz':
        # Load multiple arrays from a .npz file
        data = np.load(file_path, allow_pickle=True)
        # npz files can contain multiple arrays, return as a dictionary
        return {file: data[file] for file in data.files}
    elif file_extension == 'pkl':
        # Load pickled data
        import pickle
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    else:
        raise ValueError("Unsupported file type")

# Example usage:
# Assuming you have files named 'example.npy', 'example.npz', and 'example.pkl'
# loaded_data = load_data('example.npy')
# print(loaded_data)
