import tensorflow as tf

# Create a sample tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Convert each entry in the tensor to strings
string_tensor = tf.strings.as_string(tensor)

# Create a session and evaluate the tensor to see the result (Useful for TensorFlow 1.x)
# With TensorFlow 2.x, eager execution is enabled by default, so you don't need a session
print(string_tensor.numpy())
