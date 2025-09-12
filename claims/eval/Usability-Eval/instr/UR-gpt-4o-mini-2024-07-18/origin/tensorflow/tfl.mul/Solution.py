import tensorflow as tf

# Example tensors
a = tf.constant([[1, 2, 3], [4, 5, 6]])
b = tf.constant([[7, 8, 9], [10, 11, 12]])

# Element-wise multiplication
result = tf.multiply(a, b)

# Print the result
print(result)
