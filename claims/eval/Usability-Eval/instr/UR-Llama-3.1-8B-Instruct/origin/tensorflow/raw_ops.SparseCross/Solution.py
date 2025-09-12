import tensorflow as tf

# Define sparse and dense tensors
indices = [[0, 0], [1, 0], [2, 1]]
values = [1.0, 2.0, 3.0]
dense_shape = [3, 2]
dense_tensor = tf.constant([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]])

# Create sparse tensor from indices and values
sparse_tensor = tf.SparseTensor(indices, values, dense_shape)

# Create other sparse and dense tensors
sparse_indices2 = [[0, 0], [1, 0], [2, 1]]
sparse_values2 = [4.0, 5.0, 6.0]
dense_shape2 = [3, 2]
dense_tensor2 = tf.constant([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]])

sparse_tensor2 = tf.SparseTensor(sparse_indices2, sparse_values2, dense_shape2)

# Stack sparse and dense tensors along a specified axis
axis = 0
stacked_tensors = tf.sparse.add(sparse_tensor, sparse_tensor2)
stacked_dense_tensors = tf.add(dense_tensor, dense_tensor2)
stacked_tensors = tf.stack([stacked_tensors, stacked_dense_tensors], axis=axis)

print(stacked_tensors)

# Convert stacked tensors back to dense format
dense_output = tf.sparse.to_dense(stacked_tensors)

# Print dense output
print(dense_output)
