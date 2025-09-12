
import tensorflow as tf

params = tf.constant([[1, 2], [3], [4, 5, 6]])
slices = tf.ragged.constant([[0], [2, 1]])
indices = tf.ragged.constant([[0], [2]])
output = tf.RaggedGather(params=params, indices=indices, name='ragged_gather_example')
print(output)
