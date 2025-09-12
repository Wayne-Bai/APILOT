import pandas as pd
import pickle

# Load the pickled pandas object from a file
def load_pickled_pandas_object(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

# Example usage
file_path = 'path/to/your/pickled_object.pkl'
data = load_pickled_pandas_object(file_path)
print(data.head())  # Display the first few rows of the data
