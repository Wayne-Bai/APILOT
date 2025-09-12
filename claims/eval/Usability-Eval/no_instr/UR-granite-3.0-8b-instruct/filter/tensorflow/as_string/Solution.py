import tensorflow as tf

# Assuming 'tensor' is your input tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Convert each entry in the tensor to strings
string_tensor = tf.strings.as_string(tensor)

# Print the resulting tensor
print(string_tensor)
