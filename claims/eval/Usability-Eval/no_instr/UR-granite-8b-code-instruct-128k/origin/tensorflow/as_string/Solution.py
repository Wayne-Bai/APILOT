import tensorflow as tf

# Create a tensor of strings
tensor = tf.constant(["hello", "world", "how", "are", "you"])

# Use tf.py_function to convert each string to its ASCII code
ascii_codes = tf.py_function(lambda x: [ord(c) for c in x], [tensor], tf.int32)

# Convert the ASCII codes back to strings
strings = tf.py_function(lambda x: [chr(c) for c in x], [ascii_codes], tf.string)

# Print the resulting strings
print(strings.numpy())
