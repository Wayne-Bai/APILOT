import tensorflow as tf

# Create two tensors to multiply
a = tf.constant([1, 2, 3], dtype=tf.float32)
b = tf.constant([4, 5, 6], dtype=tf.float32)

# Perform element-wise multiplication
c = tf.multiply(a, b)

# Print the result
print(c)
