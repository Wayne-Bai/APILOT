import tensorflow as tf

# Define the parameters
params = tf.ragged.constant([[1, 2, 3], [4, 5], [6, 7, 8, 9]])

# Define the indices
indices = tf.constant([[0, 1], [1, 0, 1]])

# Use tf.gather_ragged to gather slices from params
gathered_params = tf.gather_ragged(params, indices, axis=0)

print(gathered_params)
