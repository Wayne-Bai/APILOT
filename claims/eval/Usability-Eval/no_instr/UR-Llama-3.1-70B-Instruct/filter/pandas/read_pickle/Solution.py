import pandas as pd
import pickle

def load_pickled_object(file_path):
    """
    Loads a pickled pandas object (or any object) from a file.

    Args:
        file_path (str): The path to the pickled object file.

    Returns:
        object: The loaded pickled object.
    """
    try:
        with open(file_path, 'rb') as file:
            pickled_object = pickle.load(file)
            return pickled_object
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
pickled_object = load_pickled_object('pickled_object.pkl')
if isinstance(pickled_object, pd.DataFrame):
    print("Loaded pickled pandas DataFrame:")
    print(pickled_object.head())
else:
    print("Loaded pickled object:")
    print(pickled_object)
