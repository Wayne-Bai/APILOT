import tensorflow as tf

# Let's say this is your parameters tensor
params = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# And these are your indices
indices = tf.constant([[0, 1], [2, 2]])

# Use tf.gather to fetch elements from the params tensor at these indices
result = tf.gather(params, indices, axis=0)

print(result)
