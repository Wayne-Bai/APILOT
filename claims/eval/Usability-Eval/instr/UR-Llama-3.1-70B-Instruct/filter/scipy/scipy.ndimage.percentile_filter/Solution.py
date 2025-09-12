import scipy.ndimage as ndi
import numpy as np

# Create a sample array
arr = np.random.randint(0, 100, size=(10, 10))

# Define the size of the filter
size = 3

# Calculate the multidimensional percentile filter
percentile = 50  # 50th percentile (median)
result = ndi.generic_filter(arr, np.nanpercentile, size=size, extra_arguments=(percentile,))

# Alternative way using percentile function
def calculate_percentile(arr, percentile):
    return np.nanpercentile(arr, percentile)

result_alt = ndi.generic_filter(arr, calculate_percentile, size=size, extra_arguments=(percentile,))

# Print the results
print("Original array:")
print(arr)
print("\nResult using np.nanpercentile:")
print(result)
print("\nResult using custom function:")
print(result_alt)
