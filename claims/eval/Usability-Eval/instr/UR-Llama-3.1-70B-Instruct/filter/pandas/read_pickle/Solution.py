# Import the pandas library and the pickle module
import pandas as pd
import pickle

# Define a function to load a pickled pandas object from a file
def load_pickled_object(file_path):
    try:
        # Use the pickle.load function to deserialize the object from a file
        with open(file_path, 'rb') as file:
            pickled_object = pickle.load(file)
            return pickled_object
    except FileNotFoundError:
        print("The file does not exist")
        return None
    except pickle.UnpicklingError:
        print("The file is not a valid pickled object")
        return None
    except Exception as e:
        print("An error occurred: ", str(e))
        return None

# Example usage:
if __name__ == "__main__":
    # Load pickled pandas object from file
    pickled_file_path = 'pickled_object.pkl'
    loaded_object = load_pickled_object(pickled_file_path)

    if loaded_object is not None:
        print("Type of loaded object: ", type(loaded_object))

        # Check if it's a pandas DataFrame
        if isinstance(loaded_object, pd.DataFrame):
            print("Loaded object is a pandas DataFrame")
            print(loaded_object.head())
