
import tensorflow as tf

# Create example sparse and dense tensors
indices = tf.constant([[0, 0], [1, 2], [2, 3]], dtype=tf.int64)
values = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
dense = tf.constant([[4.0, 5.0], [6.0, 7.0], [8.0, 9.0]], dtype=tf.float32)
shapes = tf.constant([3, 4], dtype=tf.int64)

# Generate sparse cross
sparse_cross = tf.raw_ops.SparseCross(sp_inputs=[indices, values], dense_inputs=dense, shapes=shapes)
