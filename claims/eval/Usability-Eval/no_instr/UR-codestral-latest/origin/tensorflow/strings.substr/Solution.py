import tensorflow as tf

# Assume the following tensor of strings
input_tensor = tf.constant(["Hello, TensorFlow!", "I love programming.", "Learning is fun."])

# Define the start position and length of the substrings
pos = 7
len = 11

# Use tf.strings.substr to get substrings
substrings = tf.strings.substr(input_tensor, pos, len)

# Print the substrings
print(substrings)
