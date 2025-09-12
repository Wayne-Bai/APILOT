import pandas as pd

def load_pickled_object(file_path):
    """
    Load pickled object from file.

    Args:
        file_path (str): The path to the pickled object file.

    Returns:
        object: The loaded pickled object.
    """
    try:
        # Use pd.read_pickle to load the pickled object
        loaded_object = pd.read_pickle(file_path)
        return loaded_object
    except pickle.UnpicklingError as e:
        # Handle any unpickling errors that might occur
        print(f"Error loading object from file: {e}")
        return None
    except Exception as e:
        # Handle any other exceptions that might occur
        print(f"An error occurred: {e}")
        return None

# Example usage:
file_path = 'path_to_your_pandas_object.pkl'
loaded_pandas_object = load_pickled_object(file_path)
if loaded_pandas_object is not None:
    # Print the first few rows of the loaded pandas object
    print(loaded_pandas_object.head())
