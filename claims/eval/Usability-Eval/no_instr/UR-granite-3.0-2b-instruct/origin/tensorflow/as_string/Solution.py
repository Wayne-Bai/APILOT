import tensorflow as tf

# Create a tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Convert each entry in the tensor to strings
string_tensor = tf.strings.as_string(tensor)

# Print the string tensor
print(string_tensor.numpy())
