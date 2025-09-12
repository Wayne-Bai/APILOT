import tensorflow as tf

# Define the parameters
params = tf.ragged.constant([[1, 2, 3], [4, 5], [6]])
indices = tf.constant([[0, 1], [2, 2], [1, 0]])

# Use tf.gather_ragged to gather the slices
gather_result = tf.gather_ragged(params, indices)

print(gather_result.to_list())  # Output: [[3, 5], [3, 1], [5, 1]]
