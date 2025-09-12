
import tensorflow as tf
ragged_tensor = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
sparse_tensor = tf.sparse.from_ragged(ragged_tensor)
print(sparse_tensor)
