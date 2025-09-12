import tensorflow as tf

# Define two tensors
x = tf.constant([1, 2, 3, 4, 5], dtype=tf.float32)
y = tf.constant([2, 3, 4, 5, 6], dtype=tf.float32)

# Element-wise multiplication
result = tf.multiply(x, y)

print(result)
