import tensorflow as tf

def reshape_sparse_tensor(sparse_tensor, new_shape):
    return tf.sparse.reshape(sparse_tensor, new_shape)

# Example usage
indices = [[0, 0], [1, 2], [2, 1]]
values = [1, 2, 3]
dense_shape = [3, 4]

sparse_tensor = tf.sparse.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

new_shape = [4, 3]  # New desired dense shape
reshaped_sparse_tensor = reshape_sparse_tensor(sparse_tensor, new_shape)

# To output the reshaped sparse tensor
print("Reshaped SparseTensor:", reshaped_sparse_tensor)
