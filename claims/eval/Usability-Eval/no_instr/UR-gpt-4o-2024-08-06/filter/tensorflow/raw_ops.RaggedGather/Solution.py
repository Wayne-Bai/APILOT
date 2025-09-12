import tensorflow as tf

# Sample data for `params`
params = tf.ragged.constant([[1, 2, 3], [4, 5], [6], [7, 8, 9, 10]])

# Indices to gather ragged slices
indices = tf.constant([0, 2, 3])

# Gather ragged slices from params axis 0 according to indices
gathered_slices = tf.gather(params, indices, axis=0)

# Converting the result to numpy for a clearer print format in eager execution
print(gathered_slices.numpy())
