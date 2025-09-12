import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=tf.quint8)

# Define the bias tensor
bias_tensor = tf.constant([[1.0], [2.0]], dtype=tf.quint8)

# Add the bias to the input tensor
result_tensor = tf.raw_ops.AddV2(input_tensor, bias_tensor)

# Print the result
print(result_tensor)
