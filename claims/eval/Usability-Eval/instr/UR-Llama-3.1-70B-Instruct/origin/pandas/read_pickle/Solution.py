# Import necessary libraries
import pandas as pd
import pickle

# Load pickled pandas object from file
def load_pickled_object(file_path):
    """
    Loads a pickled pandas object from a file.

    Args:
    file_path (str): The path to the file containing the pickled object.

    Returns:
    object: The loaded pickled object.
    """
    try:
        with open(file_path, 'rb') as file:
            loaded_object = pickle.load(file)
            return loaded_object
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except pickle.UnpicklingError:
        print(f"Failed to unpickle object from file {file_path}.")
        return None

# Example usage:
if __name__ == "__main__":
    file_path = 'pickled_object.pkl'  # replace with your file path
    loaded_object = load_pickled_object(file_path)
    if loaded_object is not None:
        print("Loaded object:")
        print(loaded_object)
