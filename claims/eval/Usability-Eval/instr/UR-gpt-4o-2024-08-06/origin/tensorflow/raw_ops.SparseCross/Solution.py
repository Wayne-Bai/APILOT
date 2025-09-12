import tensorflow as tf

# Define input sparse tensors
sp_tensor1 = tf.SparseTensor(indices=[[0, 0], [1, 2]],
                             values=[1, 2],
                             dense_shape=[3, 4])

sp_tensor2 = tf.SparseTensor(indices=[[0, 1], [2, 3]],
                             values=[3, 4],
                             dense_shape=[3, 4])

# Define input dense tensors
dense_tensor1 = tf.constant([[5, 6], [7, 8], [9, 10]])
dense_tensor2 = tf.constant([[11, 12], [13, 14], [15, 16]])

# Use tf.sparse.cross, which performs a similar functionality to the SparseCross method
sparse_tensors_input = [sp_tensor1, sp_tensor2]
dense_tensors_input = [dense_tensor1, dense_tensor2]

# Generate sparse and dense crosses
sparse_result = tf.sparse.cross(sparse_tensors_input)
dense_result = tf.concat(dense_tensors_input, axis=1)

# Sparse results need to be dealt as Sparse Tensors
dense_cross_result = tf.sparse.to_dense(sparse_result)

# Print the results
print("Sparse Cross Result (dense format):")
print(dense_cross_result.numpy())
print("\nDense Concat Result:")
print(dense_result.numpy())
