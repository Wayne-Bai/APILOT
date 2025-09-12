import numpy as np

# Load data from a text file
def load_data(file_path):
    data = np.loadtxt(file_path)
    return data

# Call the function
file_path = 'your_file_path.txt'  # Replace with your file path.
data = load_data(file_path)

# Print the data
print(data)
