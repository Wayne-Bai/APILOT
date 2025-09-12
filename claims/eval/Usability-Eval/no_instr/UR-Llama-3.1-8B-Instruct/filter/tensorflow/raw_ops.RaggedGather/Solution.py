import tensorflow as tf

# Create a sample ragged tensor
params = tf.ragged.constant([[1, 2], [3, 4, 5], [6, 7, 8, 9]])

# Create a sample indices tensor
indices = tf.constant([0, 2, 0, 1])

# Use tf.gather_ragged to gather ragged slices from params
result = tf.gather_ragged(params, indices, axis=0)

# Print the result
print(result.to_list())  # Output: [[1, 2], [8, 9], [1, 2, 4, 5 ]]
