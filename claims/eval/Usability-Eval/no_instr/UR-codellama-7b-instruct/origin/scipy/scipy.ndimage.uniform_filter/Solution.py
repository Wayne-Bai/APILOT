
import numpy as np
from scipy import signal

# Define the parameters for the multidimensional uniform filter
n = [2, 3]  # Dimensions of the filter
h = [[0.5, 0.5], [0.5, 0.5]]  # Correlation matrix of the filter

# Generate a 2D array with random data
data = np.random.rand(10, 10)

# Apply the multidimensional uniform filter to the data
filtered_data = signal.uniform_filter(data, size=n, mode='reflect', cval=0.0, correlation_matrix=h)

print("Filtered data:")
print(filtered_data)
