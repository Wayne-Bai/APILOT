import tensorflow as tf

# Define a SparseTensor
indices = tf.constant([[0, 0], [1, 2], [2, 3]], dtype=tf.int64)
values = tf.constant([1, 2, 3], dtype=tf.int32)
dense_shape = tf.constant([3, 4], dtype=tf.int64)

sparse_tensor = tf.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

# Choose the dimension along which to split the sparse tensor
axis = 1
num_split = 2

# Split the SparseTensor
sparse_tensors_split = tf.sparse.split(sp_input=sparse_tensor, num_split=num_split, axis=axis)

# Print the results
print("Split Sparse Tensors:")
for sparse_part in sparse_tensors_split:
    print(tf.sparse.to_dense(sparse_part).numpy())
