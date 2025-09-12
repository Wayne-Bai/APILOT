import tensorflow as tf

# Create a Tensor of strings
strings = tf.constant(["hello", "world", "how", "are", "you"])

# Define the start and end indices of the substrings you want to extract
start_indices = tf.constant([1, 0, 0, 0, 0])
end_indices = tf.constant([2, 1, 3, 5, 5])

# Extract the substrings using string slicing
substrings = tf.strings.slice(strings, start_indices, end_indices)

# Print the result
print(substrings)
