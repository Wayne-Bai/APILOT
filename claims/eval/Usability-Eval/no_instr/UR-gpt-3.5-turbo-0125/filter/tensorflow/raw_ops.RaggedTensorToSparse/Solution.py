
import tensorflow as tf

def ragged_tensor_to_sparse(ragged_tensor):
    flat_values = ragged_tensor.flat_values
    row_splits = ragged_tensor.row_splits
    indices = tf.expand_dims(tf.range(tf.size(flat_values)), axis=1)
    row_lengths = tf.gather(row_splits, tf.range(row_splits.shape[0]-1))
    row_indices = tf.repeat(tf.range(row_lengths.shape[0]), row_lengths)
    indices = tf.expand_dims(tf.concat([row_indices[:, tf.newaxis], indices], axis=1), axis=1)
    values = tf.expand_dims(flat_values, axis=1)
    dense_shape = [row_lengths.shape[0], tf.reduce_max(indices[:, 1]) + 1]
  
    return tf.sparse.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

ragged_tensor = tf.RaggedTensor.from_value_rowids(values=[10, 20, 30, 40, 50, 60], value_rowids=[0, 0, 1, 1, 2, 2])
sparse_tensor = ragged_tensor_to_sparse(ragged_tensor)
print(sparse_tensor)
