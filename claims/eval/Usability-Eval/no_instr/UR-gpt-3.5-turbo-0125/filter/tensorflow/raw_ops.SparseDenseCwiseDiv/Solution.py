
import tensorflow as tf

def sparse_tensor_divide(sparse_tensor, dense_tensor):
    result = tf.sparse.sparse_dense_divide(sparse_tensor, dense_tensor)
    return result
