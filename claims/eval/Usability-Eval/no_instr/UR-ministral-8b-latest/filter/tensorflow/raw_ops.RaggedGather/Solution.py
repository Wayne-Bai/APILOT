import tensorflow as tf

def gather_ragged_slices(params, indices, axis=0):
    # Gather ragged slices from 'params' axis 'axis' according to 'indices'
    with tf.raw_ops.GatherRaw(ragged_params=params, indices=indices, axis=axis):
        gathered_slices = tf.raw_ops.NaiveDynamicRaggedSlice(params=params, indices=indices, begin_indices=tf.constant([], dtype=tf.int64), axis=axis, validate_indicator_keys=True)
    return gathered_slices

# Example usage
# Define some ragged tensors
params = tf.Variable([[1, 2], [3, 4, 5], [6, 7, 8], [9, 10]])
indices = [[0, 2]]

# Gather slices
gathered_slices = gather_ragged_slices(params, indices)
print(gathered_slices)
