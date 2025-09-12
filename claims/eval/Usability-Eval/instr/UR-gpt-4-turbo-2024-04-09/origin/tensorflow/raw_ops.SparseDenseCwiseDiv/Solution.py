import tensorflow as tf

def divide_sparse_by_dense(sparse_tensor, dense_tensor):
    # Convert the sparse tensor to a dense format
    sparse_tensor_dense = tf.sparse.to_dense(sparse_tensor)

    # Element-wise division of the dense representations
    result_dense = tf.math.divide(sparse_tensor_dense, dense_tensor)

    # Convert the result back to a SparseTensor, keeping only non-zero entries
    result_sparse = tf.sparse.from_dense(result_dense)

    return result_sparse

# Example usage:
# Create a SparseTensor
indices = [[0, 0], [1, 2]]
values = [1, 2]
dense_shape = [3, 4]
sparse_tensor = tf.sparse.SparseTensor(indices, values, dense_shape)

# Create a dense tensor
dense_tensor = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Divide sparse tensor by dense tensor
result = divide_sparse_by_dense(sparse_tensor, dense_tensor)
print(tf.sparse.to_dense(result))
