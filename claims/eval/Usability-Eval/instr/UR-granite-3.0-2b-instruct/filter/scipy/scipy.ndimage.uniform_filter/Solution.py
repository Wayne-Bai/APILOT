from scipy.ndimage import uniform_filter

# Define the input multidimensional array
input_array = ...

# Define the filter size
filter_size = ...

# Apply the uniform filter
filtered_array = uniform_filter(input_array, size=filter_size)
