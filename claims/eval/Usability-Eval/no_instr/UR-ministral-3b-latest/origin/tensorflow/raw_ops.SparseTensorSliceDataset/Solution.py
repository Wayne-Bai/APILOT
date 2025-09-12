import tensorflow as tf

# Assume we have a SparseTensor
data = tf.constant([[1, 0, 2], [0, 3, 4], [5, 0, 7]], dtype=tf.int64)
indices = tf.constant([[0, 0], [1, 1]], dtype=tf.int64)
sparse_tensor = tf.SparseTensor(indices, data, [3, 4])

# Split a SparseTensor into elements row-wise
elements = sparse_tensor.to_tensor(dense_tensor=False).to_sparse()
for i in range(elements.tree_node_shape[1]):
    print(elements[i] if i < elements.tree_node_count else None)
