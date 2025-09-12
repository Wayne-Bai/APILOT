import tensorflow as tf

# Create a sample tensor
params = tf.constant([[1, 2], [3, 4], [5, 6], [7, 8]])

# Indices we want to gather
indices = tf.constant([0, 2])

# Use tf.gather to gather slices based on indices
result = tf.gather(params, indices)

# To run the operation in eager execution, simply print the result
print(result)
