import tensorflow as tf

# Create a sample tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Convert each entry in the tensor to a string using tf.strings.as_string
string_tensor = tf.strings.as_string(tensor)

# Start a TensorFlow session and evaluate the tensor
# Note: In TensorFlow 2.x, eager execution is enabled by default, so you can simply print
# the result directly without creating a session.
print(string_tensor.numpy())
