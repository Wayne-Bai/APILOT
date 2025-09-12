import tensorflow as tf

def fill_empty_rows(sparse_tensor, default_value):
    filled_tensor, _ = tf.sparse.fill_empty_rows(sparse_tensor, default_value)
    return filled_tensor

# Example usage
values = [1, 2, 3]
indices = [[0, 0], [2, 1], [3, 3]]
dense_shape = [4, 4]
sparse_tensor = tf.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)
default_value = -1

filled_sparse_tensor = fill_empty_rows(sparse_tensor, default_value)
print(tf.sparse.to_dense(filled_sparse_tensor))
