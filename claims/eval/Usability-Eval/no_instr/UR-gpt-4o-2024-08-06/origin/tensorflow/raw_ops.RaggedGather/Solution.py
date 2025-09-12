import tensorflow as tf

# Define the parameters (ragged tensor) from which you want to gather slices
params = tf.ragged.constant([[1, 2, 3], [4, 5], [6], [7, 8, 9, 10]])

# Define the indices of the slices you'd like to gather
indices = tf.constant([0, 2, 3])

# Gather ragged slices using the RaggedGather operation
gathered_slices = tf.gather(params, indices)

# Convert to a normal tensor if needed or just view the result as a ragged tensor
print(gathered_slices.to_list())  # Output the gathered ragged slices
