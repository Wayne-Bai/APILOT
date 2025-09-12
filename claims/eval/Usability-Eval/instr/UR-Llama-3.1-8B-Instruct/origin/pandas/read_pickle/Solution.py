# Import necessary libraries
import pandas as pd

# Define the filename that stores the pickled pandas object
filename = 'data.pkl'

# Use pd.read_pickle() function to load the pickled pandas object from the file
def load_pickled_object(filename):
    """
    Load a pickled object from a file.

    Parameters:
    filename (str): The name of the file that stores the pickled object.

    Returns:
    object: The loaded pickled object.
    """
    try:
        obj = pd.read_pickle(filename)
        return obj
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return None

# Call the function to load the pickled pandas object
pickled_df = load_pickled_object(filename)

# Check if the object is loaded successfully
if pickled_df is not None:
    print(pickled_df.head())  # Print the first few rows of the loaded pandas object
else:
    print("Failed to load the pickled object.")
