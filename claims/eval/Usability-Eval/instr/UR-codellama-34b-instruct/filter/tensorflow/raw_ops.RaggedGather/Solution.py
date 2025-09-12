import tensorflow as tf

# Define the input tensors
params = tf.constant([[1, 2], [3, 4]])
indices = tf.constant([[0], [0]])

# Gather ragged slices from params axis 0 according to indices
output = tf.raw_ops.Gather(params=params, indices=indices)

print(output)
