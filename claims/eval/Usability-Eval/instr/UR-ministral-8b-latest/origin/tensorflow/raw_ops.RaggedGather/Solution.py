import tensorflow as tf

# Define an example TensorFlow ragged tensor
params = tf.ragged.constant([[1], [2], [3], [4], [5]], dtype=tf.int32)

# Define the indices
indices = tf.constant([0, 2, 4], dtype=tf.int32)

# Gather the ragged slices from `params` axis 0 according to indices
gathered = tf.raw_ops.Gather(params, params, indices)

# Print the result
print(gathered)
