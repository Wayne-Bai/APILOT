
import tensorflow as tf
indices = tf.constant([[3, 2, 0, 1], [0, 1, 2, 3]])

tuples = tf.unstack(indices, axis=1)

print(tuples)
