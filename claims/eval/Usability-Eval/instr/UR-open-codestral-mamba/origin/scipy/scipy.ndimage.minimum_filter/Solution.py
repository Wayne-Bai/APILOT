from scipy.ndimage import minimum_filter

# Input multidimensional array
x = np.array([[2, 3, 5, -8],
              [2, 4, -12, 3],
              [-4, 4, -1, -7],
              [-7, -2, 1, 1]])

# Define the size of the minimum filter
size = (2, 2)

# Apply minimum filter
min_filtered_array = minimum_filter(x, size)

# Output the result
print(min_filtered_array)
