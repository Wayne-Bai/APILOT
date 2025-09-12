
import tensorflow as tf

def ragged_tensor_to_sparse(ragged_tensor):
    values = ragged_tensor.flat_values
    indices = ragged_tensor.value_rowids()

    dense_shape = ragged_tensor.bounding_shape()
    
    return tf.sparse.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)
