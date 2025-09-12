import tensorflow as tf

def reshape_sparse_tensor(sparse_tensor, new_shape):
    # Ensure the input is a SparseTensor
    if not isinstance(sparse_tensor, tf.SparseTensor):
        raise ValueError("Input must be a SparseTensor")
    
    # Get the indices, values, and dense shape of the SparseTensor
    indices = sparse_tensor.indices
    values = sparse_tensor.values
    dense_shape = sparse_tensor.dense_shape
    
    # Reshape the indices to the new shape
    new_indices = tf.sparse.reshape(sparse_tensor, new_shape).indices
    
    # Create a new SparseTensor with the reshaped indices and the same values
    reshaped_sparse_tensor = tf.SparseTensor(indices=new_indices, values=values, dense_shape=new_shape)
    
    return reshaped_sparse_tensor

# Example usage:
# Assuming `sparse_tensor` is a SparseTensor with shape [4, 6]
# and `new_shape` is [2, 12]
sparse_tensor = tf.SparseTensor(indices=[[0, 0], [1, 2], [3, 4]], values=[1, 2, 3], dense_shape=[4, 6])
new_shape = [2, 12]

reshaped_sparse_tensor = reshape_sparse_tensor(sparse_tensor, new_shape)
print(reshaped_sparse_tensor)
