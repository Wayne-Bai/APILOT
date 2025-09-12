import tensorflow as tf

def ragged_to_sparse(ragged_tensor):
    # Get the values from the RaggedTensor
    values = ragged_tensor.flat_values
    
    # Get the nested row splits
    row_splits = ragged_tensor.nested_row_splits
    
    # Calculate the indices for the SparseTensor
    indices = []
    for i, splits in enumerate(row_splits):
        for j in range(len(splits) - 1):
            for k in range(splits[j], splits[j + 1]):
                indices.append([i, j, k - splits[j]])
    
    # Create the SparseTensor
    sparse_tensor = tf.SparseTensor(
        indices=indices,
        values=values,
        dense_shape=ragged_tensor.bounding_shape()
    )
    
    return sparse_tensor

# Example usage:
# ragged_tensor = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
# sparse_tensor = ragged_to_sparse(ragged_tensor)
# print(sparse_tensor)
