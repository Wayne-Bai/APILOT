
import tensorflow as tf

def sparse_reshape(sparse_tensor, new_shape):
    return tf.raw_ops.SparseReshape(input_indices=sparse_tensor.indices,
                                     input_values=sparse_tensor.values,
                                     input_shape=sparse_tensor.dense_shape,
                                     new_shape=new_shape)
