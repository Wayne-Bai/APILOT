import tensorflow as tf

# Assuming 'indices' is a 1D tensor of flat indices
indices = tf.constant([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Convert flat indices into a tuple of coordinate arrays
coordinates = tf.raw_ops.ScatterGatherND(indices=indices)

print(coordinates)
