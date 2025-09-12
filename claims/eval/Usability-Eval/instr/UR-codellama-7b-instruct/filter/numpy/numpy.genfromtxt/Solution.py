
import numpy as np

# Load the data from the text file
data = np.genfromtxt('data.txt', delimiter=',')

# Handle missing values by assigning them to NaN (not a number)
data[np.isnan(data)] = np.nan

# Print the modified data
print(data)
