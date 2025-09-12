import numpy as np

# Open the file and read the contents
with open('data.txt', 'r') as f:
    # Use numpy to load the data into a 2D array
    data = np.loadtxt(f, dtype=int, skiprows=1)

# Handle missing values by replacing them with the mean of the column
mean = np.mean(data[:, 0])
np.where(data == -1, mean, data)
