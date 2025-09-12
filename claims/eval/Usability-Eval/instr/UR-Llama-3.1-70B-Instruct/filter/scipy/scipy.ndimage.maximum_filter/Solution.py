import scipy.ndimage as ndi
import numpy as np

# Generate a random 3D array
np.random.seed(0)
data = np.random.randint(0, 100, (5, 5, 5))

# Calculate a 3D maximum filter
max_filtered_data = ndi.maximum_filter(data, size=3)

# Calculate a 3D maximum filter with footprint (other elements are ignored)
footprint = np.ones((2, 2, 2))
max_filtered_data_footprint = ndi.maximum_filter(data, footprint=footprint)

# Print original data and max filtered data
print("Original Data:")
print(data)

print("\n3D Maximum Filtered Data:")
print(max_filtered_data)

print("\n3D Maximum Filtered Data with Footprint:")
print(max_filtered_data_footprint)
