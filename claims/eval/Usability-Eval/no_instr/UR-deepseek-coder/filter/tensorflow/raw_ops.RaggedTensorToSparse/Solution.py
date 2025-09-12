import tensorflow as tf

def ragged_to_sparse(ragged_tensor):
    # Get the values from the RaggedTensor
    values = ragged_tensor.flat_values
    
    # Get the nested row splits
    row_splits = ragged_tensor.nested_row_splits
    
    # Create the indices for the SparseTensor
    indices = tf.ragged.stack_dynamic_partitions(
        tf.range(tf.size(values)),
        tf.ragged.boolean_mask(tf.range(tf.size(values)), ragged_tensor.value_rowids()),
        ragged_tensor.nrows()
    )
    
    # Convert the indices to a dense tensor
    indices = indices.to_tensor()
    
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
