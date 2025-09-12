from scipy.ndimage import maximum_filter
import numpy as np

# Define an example 2D array
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Define the size of the maximum filter window
size = 2

# Apply the maximum filter
max_filtered = maximum_filter(data, size)

print(max_filtered)
