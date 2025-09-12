import tensorflow as tf

def fill_sparse_tensor(sparse_tensor, default_value):
    sparse_tensor.set_shape([None, None])
    dense_tensor = tf.sparse.to_dense(sparse_tensor, default_value=default_value)
    filled_sparse_tensor = tf.sparse.from_dense(dense_tensor)
    return filled_sparse_tensor

# Example Usage
# Create a SparseTensor
indices = tf.constant([[0, 0], [1, 2]], dtype=tf.int64)
values = tf.constant([1, 2], dtype=tf.int32)
shape = tf.constant([2, 3], dtype=tf.int64)
sparse_tensor = tf.sparse.SparseTensor(indices, values, shape)

filled_sparse_tensor = fill_sparse_tensor(sparse_tensor, default_value=0)
print(tf.sparse.to_dense(filled_sparse_tensor))
