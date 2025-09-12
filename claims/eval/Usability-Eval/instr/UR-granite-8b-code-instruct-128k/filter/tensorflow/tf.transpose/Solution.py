import tensorflow as tf

# Define a variable a
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# Transpose a
a_transposed = tf.transpose(a)

# Print the result
print(a_transposed)

# Output:
# tf.Tensor(
# [[1 4]
# [2 5]
# [3 6]], shape=(3, 2), dtype=int32)