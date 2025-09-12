from scipy.ndimage import percentile_filter

# Define the input multidimensional array
input_array = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
               [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
               [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]

# Define the percentile value (e.g., 50 for median)
percentile_value = 50

# Apply the percentile filter
filtered_array = percentile_filter(input_array, percentile_value)

# Print the filtered array
print(filtered_array)
