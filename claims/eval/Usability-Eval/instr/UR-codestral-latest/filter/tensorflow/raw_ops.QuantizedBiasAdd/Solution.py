import tensorflow as tf

# Create a constant tensor for the input
input_tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0], dtype=tf.float32)

# Create a constant tensor for the bias
bias_tensor = tf.constant([1.0, 1.0, 1.0, 1.0, 1.0], dtype=tf.float32)

# Add the bias tensor to the input tensor
result_tensor = tf.add(input_tensor, bias_tensor)

# Print the result
print(result_tensor)
