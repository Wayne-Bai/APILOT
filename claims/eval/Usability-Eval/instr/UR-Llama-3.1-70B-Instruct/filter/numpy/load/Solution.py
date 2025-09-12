# Import necessary numpy module
import numpy as np

# Load a numpy array from a.npy file
def load_array_npy(filename):
    try:
        array = np.load(filename, allow_pickle=False)
        return array
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Load a numpy array or a pickled object from a.npz file
def load_array_npz(filename):
    try:
        with np.load(filename, allow_pickle=False) as data:
            return data
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Usage
if __name__ == "__main__":
    # Generate and save a numpy array to a.npy file
    array = np.random.rand(3, 3)
    np.save('example.npy', array)

    # Generate and save numpy arrays to a.npz file
    array1 = np.random.rand(3, 3)
    array2 = np.random.rand(3, 3)
    np.savez('example.npz', array1=array1, array2=array2)

    # Load the saved arrays
    loaded_array_npy = load_array_npy('example.npy')
    loaded_array_npz = load_array_npz('example.npz')

    # Print the loaded arrays
    print("Loaded.npy array: \n", loaded_array_npy)
    print("Loaded.npz arrays: ", loaded_array_npz)
