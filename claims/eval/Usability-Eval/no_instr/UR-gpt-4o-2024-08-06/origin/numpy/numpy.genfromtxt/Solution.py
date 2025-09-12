import numpy as np

# Load data from a text file while specifying how to handle missing values.
# Using numpy's genfromtxt which can handle missing data

# Assume the text file is named 'data.txt'.
# Use missing_values parameter in genfromtxt to specify how missing data is denoted (e.g., empty string)
# Use filling_values to specify the value that should be inserted for missing data (e.g., NaN)

filename = 'data.txt'
data = np.genfromtxt(filename, delimiter=',', missing_values='', filling_values=np.nan)

print(data)
