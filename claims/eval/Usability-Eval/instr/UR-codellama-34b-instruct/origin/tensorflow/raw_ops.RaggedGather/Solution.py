import tensorflow as tf

# Create a tensor of shape (3, 4)
params = tf.constant([[1, 2], [3, 4]])

# Create a tensor of indices with shape (3, 2)
indices = tf.constant([[0, 1], [1, 2], [2, 3]])

# Gather the slices from params according to indices along axis 0
slices = tf.gather(params, indices, axis=0)

print(slices) # Output: [[1, 2], [3, 4], [5, 6]]
