import tensorflow as tf

# Define a tensor of strings
tensor_of_strings = tf.constant(["Hello World", "Python TensorFlow", "Substring Example"])

# Define the start and end indices for substring extraction
start_idx = 6
end_idx = 12

# Extract substrings using tf.strings.substr
substrings = tf.strings.substr(tensor_of_strings, start_idx, end_idx - start_idx)

# Print the extracted substrings
print(substrings)
