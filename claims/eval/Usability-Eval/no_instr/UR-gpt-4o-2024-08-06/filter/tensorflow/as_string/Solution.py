import tensorflow as tf

# Create a sample tensor of various types
tensor = tf.constant([1, 2, 3, 4, 5], dtype=tf.int32)

# Convert each entry in the tensor to string
tensor_as_strings = tf.strings.as_string(tensor)

# Print the result
print(tensor_as_strings)
