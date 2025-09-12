import tensorflow as tf

# Creating sample parameters tensor
params = tf.random.normal([5, 5])

# Creating sample indices tensor
indices = tf.constant([[0, 1], [2, 3, 4]])

# Using tf.raw_ops.Gather to gather ragged slices from params axis 0 according to indices
gathered_params = tf.raw_ops.GatherV2(params=params, indices=indices, axis=0)
