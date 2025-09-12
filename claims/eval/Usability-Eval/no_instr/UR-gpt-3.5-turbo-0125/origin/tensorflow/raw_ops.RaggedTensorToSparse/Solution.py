
import tensorflow as tf

def ragged_to_sparse(ragged_tensor):
    # Create the indices for the SparseTensor
    indices = ragged_tensor.flat_values.indices
    
    # Create the values for the SparseTensor
    values = ragged_tensor.flat_values
    
    # Create the dense_shape for the SparseTensor
    dense_shape = ragged_tensor.bounding_shape()
    
    # Create the SparseTensor
    sparse_tensor = tf.sparse.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)
    
    return sparse_tensor

# Example usage
ragged_tensor = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
sparse_tensor = ragged_to_sparse(ragged_tensor)
print(sparse_tensor)
