# Import necessary libraries
import pandas as pd
import pickle

# Load pickled pandas object from file
def load_pickled_object(file_path):
    """
    Load a pickled pandas object (or any object) from a file.
    
    Parameters:
    file_path (str): The path to the pickled object file.
    
    Returns:
    object: The loaded pickled object.
    """
    try:
        with open(file_path, 'rb') as f:
            obj = pickle.load(f)
            return obj
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

# Example usage:
if __name__ == "__main__":
    file_path = 'pickled_object.pkl'  # Replace with your file path
    obj = load_pickled_object(file_path)
    
    # Check if the object is a pandas DataFrame
    if isinstance(obj, pd.DataFrame):
        print("Loaded DataFrame:")
        print(obj.head())
    else:
        print("Loaded object:")
        print(type(obj))
