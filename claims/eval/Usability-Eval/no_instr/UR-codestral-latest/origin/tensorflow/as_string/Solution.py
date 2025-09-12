import tensorflow as tf

# Create a simple tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Convert tensor to strings
string_tensor = tf.strings.as_string(tensor)

# Print out the result
print(string_tensor.numpy())
