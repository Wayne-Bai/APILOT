import tensorflow as tf

# Create a tensor
tensor = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Reverse variable length slices
reversed_tensor = tf.raw_ops.ReverseV2(tensor)

# Print the reversed tensor
print(reversed_tensor)
