import tensorflow as tf

# Assuming params and indices are your input tensors
params = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
indices = tf.constant([0, 1, 2])

# Gather ragged slices from params axis 0 according to indices
gathered_slices = tf.raw_ops.GatherV2(params, indices, axis=0)

print(gathered_slices)
