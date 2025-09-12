import numpy as np

# Specify the path to the text file
file_path = 'your_file_path.txt'

# Load data from a text file, replacing missing values with NaN
data = np.loadtxt(file_path, delimiter=',', dtype=float)

# Handling missing values, for example replacing NaN with a specified value such as zero
data[np.isnan(data)] = 0

print(data)
