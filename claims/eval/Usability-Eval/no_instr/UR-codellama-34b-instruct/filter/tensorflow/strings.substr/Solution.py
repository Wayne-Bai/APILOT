
import tensorflow as tf

# Create a tensor of strings
tensor_of_strings = tf.constant(['apple', 'banana', 'orange'])

# Define the indices of the characters that should be kept in the substring
indices = [1, 2, 3]

# Use TensorFlow's `string_slice` function to extract substrings from the tensor of strings
substrings = tf.string_slice(tensor_of_strings, indices)

# Print the resulting tensor of substrings
print(substrings)
