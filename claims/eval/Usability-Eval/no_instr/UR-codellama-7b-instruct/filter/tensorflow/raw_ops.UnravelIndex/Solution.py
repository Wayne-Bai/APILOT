import tensorflow as tf

# Define the input tensor
indices = tf.constant([[0, 1], [2, 3], [4, 5]])

# Use `tf.raw_ops.UnravelIndex` to convert flat indices into coordinate arrays
coordinates = tf.raw_ops.UnravelIndex(indices=indices)
