import tensorflow as tf

# Define the SparseTensor
indices = tf.constant([[0, 0], [1, 2], [2, 3]], dtype=tf.int64)
values = tf.constant([1, 2, 3], dtype=tf.float32)
dense_shape = tf.constant([3, 4], dtype=tf.int64)

sparse_tensor = tf.sparse.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

# Define the new dense shape for the reshaping
new_dense_shape = tf.constant([4, 3], dtype=tf.int64)

# Reshape the SparseTensor
reshaped_sparse_tensor = tf.sparse.reshape(sparse_tensor, new_dense_shape)

# Print the result
print("Original SparseTensor:")
print(sparse_tensor)
print("\nReshaped SparseTensor:")
print(reshaped_sparse_tensor)
