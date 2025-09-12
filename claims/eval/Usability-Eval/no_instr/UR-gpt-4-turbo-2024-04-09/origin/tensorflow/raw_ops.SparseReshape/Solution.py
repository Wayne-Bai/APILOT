import tensorflow as tf

def reshape_sparse_tensor(sparse_tensor, new_shape):
    reshaped_sparse_tensor = tf.sparse.reshape(sparse_tensor, new_shape)
    return reshaped_sparse_tensor

# Example usage
indices = [[0, 0], [1, 2]]
values = [1, 2]
dense_shape = [3, 4]

sparse_tensor = tf.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)
new_shape = [6, 2]

reshaped_sparse_tensor = reshape_sparse_tensor(sparse_tensor, new_shape)
print("Original Sparse Tensor:")
print(sparse_tensor)
print("Reshaped Sparse Tensor:")
print(reshaped_sparse_tensor)
