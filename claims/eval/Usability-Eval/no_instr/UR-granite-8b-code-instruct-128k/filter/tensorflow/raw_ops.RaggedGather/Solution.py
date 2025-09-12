
import tensorflow as tf

# Create a parameter tensor
params = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create an index tensor
indices = tf.ragged.constant([[0, 2], [1, -1]])

# Gather the ragged slices
result = tf.raw_ops.RaggedGather(params=params, indices=indices)

with tf.Session() as sess:
    print(sess.run(result))
