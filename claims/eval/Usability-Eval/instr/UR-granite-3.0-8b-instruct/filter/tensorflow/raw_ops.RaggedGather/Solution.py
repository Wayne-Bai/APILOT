import tensorflow as tf

# Assuming params and indices are defined
params = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
indices = tf.constant([0, 2])

# Gather ragged slices from params axis 0 according to indices
gathered_params = tf.raw_ops.GatherV2(params, indices, axis=0, batch_dims=0)

print(gathered_params)
