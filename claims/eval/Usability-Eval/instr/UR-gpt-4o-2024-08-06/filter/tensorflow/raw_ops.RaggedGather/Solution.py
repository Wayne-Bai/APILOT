import tensorflow as tf

# Create ragged tensor
params = tf.ragged.constant([[1, 2, 3], [], [4, 5], [6]])

# Define indices to gather
indices = tf.constant([0, 2, 1, 2])

# Use tf.gather to gather slices from params along axis 0 according to indices
result = tf.gather(params, indices, axis=0)

# Convert the result to a numpy array for easy viewing
print(result.to_list())
