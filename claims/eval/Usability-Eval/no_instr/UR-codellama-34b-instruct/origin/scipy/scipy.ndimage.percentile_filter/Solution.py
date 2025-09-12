import numpy as np
from scipy import signal

# Define the array to be filtered
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the percentage cutoff for filtering
cutoff = 0.8

# Calculate the multidimensional percentile filter using scipy.signal.rank_filter
result = signal.rank_filter(arr, cutoff, size=3)

print(result)
