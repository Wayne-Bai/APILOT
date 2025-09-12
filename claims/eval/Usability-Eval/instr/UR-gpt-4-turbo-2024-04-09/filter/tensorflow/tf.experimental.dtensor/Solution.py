import tensorflow as tf

# Example tensor initialization
tensor_a = tf.constant([[1, 2], [3, 4]], dtype=tf.int32)
tensor_b = tf.constant([[5, 6], [7, 8]], dtype=tf.int32)

# Simple addition operation
tensor_sum = tensor_a + tensor_b

print("Result of tensor addition:", tensor_sum)
