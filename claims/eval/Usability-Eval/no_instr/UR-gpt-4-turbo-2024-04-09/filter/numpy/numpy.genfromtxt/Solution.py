import numpy as np

# Define the file path
file_path = 'data.txt'

# Load data from the text file, handling missing values
data = np.genfromtxt(file_path, delimiter=',', missing_values=None, filling_values=np.nan)

print(data)
