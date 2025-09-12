import tensorflow as tf

# Define input tensor
x = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# Define slice lengths
slice_lengths = tf.constant([3, 3, 3, 3])

# Use tf.raw_ops.RevV2 to reverse slices
result = tf.raw_ops.RevV2(tensor=x, dims=[1], T=tf.int32)

# Print result
print(result.numpy())
