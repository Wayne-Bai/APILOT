import numpy as np

# Define a function to load arrays or pickled objects from.npy,.npz or pickled files
def load_array(filename):
    """
    Load arrays or pickled objects from.npy,.npz or pickled files.

    Parameters:
    filename (str): The name of the file to load.

    Returns:
    array: The loaded array or pickled object.
    """
    try:
        # Try to load the file as a numpy array
        return np.load(filename, allow_pickle=True)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
array = load_array('example.npy')
if array is not None:
    print(array)

# Load arrays from.npz file
def load_arrays(filename):
    """
    Load arrays from.npz file.

    Parameters:
    filename (str): The name of the file to load.

    Returns:
    dict: A dictionary containing the loaded arrays.
    """
    try:
        # Try to load the file as a numpy array
        return np.load(filename, allow_pickle=True)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
arrays = load_arrays('example.npz')
if arrays is not None:
    for key, value in arrays.items():
        print(f"{key}: {value}")

# Save array to.npy file
def save_array(array, filename):
    """
    Save array to.npy file.

    Parameters:
    array (numpy.ndarray): The array to save.
    filename (str): The name of the file to save to.
    """
    try:
        np.save(filename, array, allow_pickle=True)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
array = np.array([1, 2, 3])
save_array(array, 'example.npy')
