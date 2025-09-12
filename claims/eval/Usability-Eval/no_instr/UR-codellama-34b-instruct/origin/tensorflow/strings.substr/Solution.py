
import tensorflow as tf

# Create a tensor of strings
tensor = tf.constant(["hello", "world", "tensorflow"])

# Extract the first character of each string
first_char = tensor[:, 0]

# Extract the last character of each string
last_char = tensor[:, -1]

# Concatenate the first and last characters to form a new tensor of strings
new_tensor = tf.string_join(first_char, last_char)

print(new_tensor) # prints <tf.Tensor: shape=(), dtype=string, numpy=b'heltf'>
