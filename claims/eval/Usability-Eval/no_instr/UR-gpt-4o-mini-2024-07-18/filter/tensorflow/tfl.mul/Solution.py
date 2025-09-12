import tensorflow as tf

# Define two tensors
tensor_a = tf.constant([[1, 2], [3, 4]])
tensor_b = tf.constant([[5, 6], [7, 8]])

# Perform element-wise multiplication
result = tf.multiply(tensor_a, tensor_b)

# Print the result
print(result)
