import tensorflow as tf

# Create two tensors
tensor1 = tf.constant([[1, 2], [3, 4]])
tensor2 = tf.constant([[5, 6], [7, 8]])

# Perform element-wise multiplication
result = tf.multiply(tensor1, tensor2)

# Print the result
print(result)
