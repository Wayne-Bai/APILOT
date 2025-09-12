import scipy

# Define the input array
input_array = scipy.random.rand(3,3)

# Define the size of the uniform filter
size = 3

# Apply the uniform filter
output_array = scipy.signal.uniform_filter(input_array, size=size)

# Print the output array
print(output_array)
