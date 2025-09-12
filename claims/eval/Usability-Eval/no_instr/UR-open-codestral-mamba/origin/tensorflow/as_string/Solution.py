import tensorflow as tf

# Create a tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Convert each entry to strings
string_tensor = tf.strings.as_string(tensor, result_type='Dense')

# Print the resulting tensor
print(string_tensor)
