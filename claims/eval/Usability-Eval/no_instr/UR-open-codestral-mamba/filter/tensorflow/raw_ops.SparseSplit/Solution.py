import tensorflow as tf

# Create a sparse tensor
indices = tf.constant([[1, 0], [2, 1], [3, 3]])
values = tf.constant([1, 2, 3])
shape = tf.constant([4, 4])
dense = tf.SparseTensor(indices, values, shape)

# Split the sparse tensor
split_num = 2
split_indices = tf.squeeze(tf.split(dense.values, split_num, axis=0), axis=-1)
split_values = tf.split(dense.values, split_num, axis=0)
split_shape = tf.constant([2, 4])
split_sparse_tensors = [tf.SparseTensor(split_indices[i], split_values[i], split_shape) for i in range(split_num)]

# Print the split sparse tensors
for split_sparse_tensor in split_sparse_tensors:
    print(split_sparse_tensor)
