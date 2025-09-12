import numpy as np

# Load arrays or pickled objects from.npy files
def load_npy_file(file_path):
    try:
        return np.load(file_path, allow_pickle=True)
    except FileNotFoundError:
        print("The file does not exist.")
        return None
    except Exception as e:
        print("An error occurred: ", str(e))
        return None

# Load arrays or pickled objects from.npz files
def load_npz_file(file_path):
    try:
        return np.load(file_path, allow_pickle=True)
    except FileNotFoundError:
        print("The file does not exist.")
        return None
    except Exception as e:
        print("An error occurred: ", str(e))
        return None

# Load arrays or pickled objects from pickled files
def load_pickled_file(file_path):
    try:
        return np.load(file_path, allow_pickle=True)
    except FileNotFoundError:
        print("The file does not exist.")
        return None
    except Exception as e:
        print("An error occurred: ", str(e))
        return None

# Example usage
if __name__ == "__main__":
    # Create an array
    array = np.array([1, 2, 3, 4, 5])

    # Save the array to an.npy file
    np.save('array.npy', array)

    # Save the array to an.npz file
    np.savez('array.npz', array=array)

    # Save the array to a pickled file
    np.save('array.pkl', array, allow_pickle=True)

    # Load the array from the.npy file
    loaded_array_npy = load_npy_file('array.npy')
    print("Loaded array from.npy file: ", loaded_array_npy)

    # Load the array from the.npz file
    loaded_array_npz = load_npz_file('array.npz')
    print("Loaded array from.npz file: ", loaded_array_npz['array'])

    # Load the array from the pickled file
    loaded_array_pkl = load_pickled_file('array.pkl')
    print("Loaded array from pickled file: ", loaded_array_pkl)
