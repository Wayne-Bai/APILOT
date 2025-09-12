
import tensorflow as tf

def fill_empty_rows(sparse_input, default_value):
    filled = tf.sparse.to_dense(sparse_input, default_value=default_value)
    return tf.sparse.from_dense(filled)

# Example usage
sparse_input = tf.SparseTensor(indices=[[0, 0], [1, 1], [2, 0]], values=[1.0, 2.0, 3.0], dense_shape=[3, 2])
default_value = 0.0
filled_sparse = fill_empty_rows(sparse_input, default_value)

print(filled_sparse)
