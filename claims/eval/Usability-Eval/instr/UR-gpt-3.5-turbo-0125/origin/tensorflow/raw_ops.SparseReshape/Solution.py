
import tensorflow as tf

def reshape_sparse_tensor(sp_input_indices, sp_input_values, sp_input_shape, new_dense_shape):
    sp_input = tf.sparse.SparseTensor(sp_input_indices, sp_input_values, sp_input_shape)
    dense_output_shape = new_dense_shape
    new_indices = tf.sparse.sparse_dense_reorder(sp_input).indices
    new_values = tf.sparse.sparse_dense_reorder(sp_input).values

    new_indices = tf.cast(new_indices, tf.int64)
    new_values = tf.cast(new_values, tf.float32)

    new_sparse_tensor = tf.sparse.SparseTensor(new_indices, new_values, dense_output_shape)

    return new_sparse_tensor
