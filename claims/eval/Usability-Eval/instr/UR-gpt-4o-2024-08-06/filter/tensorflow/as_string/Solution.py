import tensorflow as tf

# Example tensor with numeric values
tensor = tf.constant([1, 2, 3, 4, 5])

# Convert each entry in the tensor to strings using map_fn
string_tensor = tf.map_fn(lambda x: tf.strings.as_string(x), tensor, dtype=tf.string)

# Start a session to run the computation (for TensorFlow 1.x)
# For TensorFlow 2.x, eager execution is enabled by default, so no session is needed
print("String tensor:", string_tensor.numpy())
