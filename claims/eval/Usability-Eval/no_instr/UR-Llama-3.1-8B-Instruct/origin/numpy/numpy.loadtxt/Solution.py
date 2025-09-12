# Import necessary libraries
import numpy as np

# Load data from the text file
def load_data(file_name):
    try:
        # Use numpy's genfromtxt function to load the data
        data = np.genfromtxt(file_name, delimiter=',', skip_header=1)
        return data
    except Exception as e:
        print("Error loading data: ", str(e))
        return None

# Test the function
file_name = "data.txt"  # Replace with your text file name
data = load_data(file_name)
if data is not None:
    print(data)
