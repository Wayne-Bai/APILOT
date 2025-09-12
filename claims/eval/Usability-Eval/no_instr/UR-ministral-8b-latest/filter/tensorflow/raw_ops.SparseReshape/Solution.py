import tensorflow as tf

# Sparse tensor example
indices = tf.constant([[0, 0], [1, 2], [2, 0]], dtype=tf.int32)
values = tf.constant([1, 2, 3], dtype=tf.float32)
shape = [3, 3]
sparse_tensor = tf.SparseTensor(indices, values, [3, 3])

# Shaping SparseTensor
reshaped_tensor = tf.raw_ops.ReshapeSparse(sparse_tensor=tf.cast(sparse_tensor, dtype=tf.string),
                                           shape=[2, 6], reshaped_name="reshaped")

print(reshaped_tensor)
