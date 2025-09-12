import numpy as np

# Load data from a text file
data = np.genfromtxt('data.txt', delimiter=',', missing_values='NA', filling_values=np.nan)

# Handle missing values (e.g., replace NaN with mean of the column)
for col in range(data.shape[1]):
    col_mean = np.nanmean(data[:, col])
    data[np.isnan(data[:, col]), col] = col_mean

print(data)
