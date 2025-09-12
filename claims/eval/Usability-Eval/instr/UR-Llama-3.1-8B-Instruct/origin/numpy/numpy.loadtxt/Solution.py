import numpy as np

# Load data from a text file into a numpy array
def load_data(file_name):
    try:
        # Use numpy.genfromtxt to Load the data from the file
        data = np.genfromtxt(file_name, delimiter=',', skip_header=1)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print("Error loading data: ", str(e))

# Example usage:
file_name = "data.txt"  # Replace with your file name
data = load_data(file_name)
print(data)
