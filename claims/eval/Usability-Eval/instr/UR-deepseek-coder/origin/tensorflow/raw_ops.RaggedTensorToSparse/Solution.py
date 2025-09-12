import tensorflow as tf

def ragged_to_sparse(ragged_tensor):
    # Get the values from the RaggedTensor
    values = ragged_tensor.values
    
    # Get the row_splits from the RaggedTensor
    row_splits = ragged_tensor.row_splits
    
    # Calculate the indices for the SparseTensor
    indices = []
    for i, splits in enumerate(row_splits[:-1]):
        for j in range(splits, row_splits[i + 1]):
            indices.append([i, j - splits])
    
    # Convert indices to a Tensor
    indices = tf.constant(indices, dtype=tf.int64)
    
    # Create the SparseTensor
    sparse_tensor = tf.SparseTensor(indices=indices, values=values, dense_shape=[len(row_splits) - 1, tf.reduce_max(row_splits)])
    
    return sparse_tensor

# Example usage:
# ragged_tensor = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
# sparse_tensor = ragged_to_sparse(ragged_tensor)
# print(sparse_tensor)
