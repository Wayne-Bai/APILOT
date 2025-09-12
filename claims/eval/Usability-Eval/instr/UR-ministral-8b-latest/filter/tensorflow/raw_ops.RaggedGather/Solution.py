import tensorflow as tf

# Example tensor and indices
param_tensor = tf.ragged.constant([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], dtype=tf.int32)
indices = [[0, 1], [1, 1]]  # Example index for axis-0

# Prepare the indices by broadcasting them as necessary
indices = tf.expand_dims(indices, axis=-1)
indices = tf.cast(indices, tf.int64)

# Gather slices according to the indices
result = tf.raw_ops.Gather(params=param_tensor, indices=indices)

# Print the result
print(result)
