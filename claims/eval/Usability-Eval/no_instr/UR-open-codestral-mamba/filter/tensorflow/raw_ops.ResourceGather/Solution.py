import tensorflow as tf

# Define the tensor slices to gather
tensor_slices = tf.Variable([[[1, 2, 3], [4, 5, 6]],
                             [[7, 8, 9], [10, 11, 12]]], dtype=tf.float32)

# Define the indices to gather
indices = tf.constant([[0, 1], [1, 0]])

# Use tf.raw_ops.GatherV2 to gather slices from tensor_slices according to indices
gathered_slices = tf.raw_ops.GatherV2(params=tensor_slices,
                                      indices=indices,
                                      axis=0)

# Print the gathered slices
print(gathered_slices)
