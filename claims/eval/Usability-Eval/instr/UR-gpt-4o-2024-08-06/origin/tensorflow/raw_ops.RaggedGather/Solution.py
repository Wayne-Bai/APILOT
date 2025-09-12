import tensorflow as tf

# Create a ragged tensor
params = tf.ragged.constant([[1, 2, 3], [4, 5], [6, 7, 8, 9]])

# Define indices to gather from params
indices = [0, 2]

# Gather ragged slices from params at the specified indices
gathered_ragged = tf.gather(params, indices)

# Execute the graph
with tf.Session() as sess:
    result = sess.run(gathered_ragged)
    print(result)
