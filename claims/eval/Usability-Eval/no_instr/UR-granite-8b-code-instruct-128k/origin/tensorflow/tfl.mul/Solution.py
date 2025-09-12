import tensorflow as tf

# Create two tensors
tensor1 = tf.constant([1, 2, 3, 4, 5], dtype=tf.float32)
tensor2 = tf.constant([5, 4, 3, 2, 1], dtype=tf.float32)

# Perform element-wise multiplication
result = tf.multiply(tensor1, tensor2)

# Print the result
print(result)
