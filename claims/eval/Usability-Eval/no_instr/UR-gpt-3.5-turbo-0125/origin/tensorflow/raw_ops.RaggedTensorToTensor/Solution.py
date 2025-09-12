
import tensorflow as tf

ragged_tensor = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])

dense_tensor = tf.raw_ops.DenseToRaggedMap(ragged_values=ragged_tensor.flat_values,
                                          ragged_row_splits=ragged_tensor.row_splits)

print(dense_tensor)
