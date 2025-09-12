import tensorflow as tf

# Define a tensor with shape (3, 4)
tensor = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Apply upper_bound on each row of the tensor
result = tf.math.reduce_min(tensor, axis=1)

print(result)  # Output: [4, 8, 12]
