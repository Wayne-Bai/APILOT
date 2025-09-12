import tensorflow as tf

def reshape_sparse_tensor(sparse_tensor, new_shape):
    """
    Reshapes a SparseTensor to a new shape.

    Args:
        sparse_tensor (tf.SparseTensor): The SparseTensor to be reshaped.
        new_shape (list or tuple): The new dense shape for the SparseTensor.

    Returns:
        tf.SparseTensor: A new SparseTensor with the specified shape.
    """
    # Convert new_shape to a Tensor
    new_shape_tensor = tf.constant(new_shape, dtype=tf.int64)

    # Create a reshaped SparseTensor
    reshaped_sparse_tensor = tf.sparse.reset_shape(sparse_tensor, new_shape_tensor)

    return reshaped_sparse_tensor

# Example usage
sparse_indices = [[0, 0], [1, 2], [2, 3]]
sparse_values = [1, 2, 3]
dense_shape = [3, 4]

# Create a SparseTensor
original_sparse_tensor = tf.SparseTensor(indices=sparse_indices, values=sparse_values, dense_shape=dense_shape)

# New shape
new_shape = [6, 2]

# Reshape the SparseTensor
reshaped = reshape_sparse_tensor(original_sparse_tensor, new_shape)

# Print the result
print("Original SparseTensor:")
print(original_sparse_tensor)

print("\nReshaped SparseTensor:")
print(reshaped)
