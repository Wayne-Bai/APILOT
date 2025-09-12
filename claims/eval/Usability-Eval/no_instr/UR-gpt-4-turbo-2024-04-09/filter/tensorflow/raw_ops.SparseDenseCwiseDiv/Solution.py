import tensorflow as tf

def sparse_dense_divide(sparse_tensor, dense_tensor):
    sp_indices = sparse_tensor.indices
    sp_values = sparse_tensor.values
    sp_dense_shape = sparse_tensor.dense_shape
    
    # Gather corresponding dense values where the sparse tensor has values
    gathered_dense_values = tf.gather_nd(dense_tensor, sp_indices)
    
    # Perform element-wise division
    new_values = tf.divide(sp_values, gathered_dense_values)
    
    # Create a new SparseTensor with the new values
    result_sparse_tensor = tf.SparseTensor(indices=sp_indices, values=new_values, dense_shape=sp_dense_shape)
    
    return result_sparse_tensor

# Example usage:
# Create SparseTensor
indices = [[0, 0], [1, 2]]
values = [8, 6]
dense_shape = [3, 4]

sparse_tensor = tf.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

# Create dense tensor
dense_tensor = tf.constant([[4, 2, 1, 3], [5, 7, 3, 8], [9, 10, 11, 12]], dtype=tf.float32)

# Perform division
result_tensor = sparse_dense_divide(sparse_tensor, dense_tensor)
print(result_tensor)
tf.sparse.to_dense(result_tensor)
