import tensorflow as tf

# Helper function to create a dense tensor from a ragged tensor
def ragged_to_dense(ragged_tensor, default_value=0):
    """Convert a ragged tensor to a dense tensor.
    
    Args:
        ragged_tensor: A tf.RaggedTensor to be converted.
        default_value: Value to use for filling empty slots in the dense tensor.
        
    Returns:
        A dense tensor.
    """
    # Optionally: find the maximum depth of the ragged tensor to determine its shape
    max_depth = ragged_tensor.flat_values.shape.rank + 1

    # Convert ragged tensor to dense tensor
    dense_tensor = ragged_tensor.to_tensor(default_value=default_value)

    return dense_tensor

# Example usage
ragged_list = [[1, 2, 3], [4], [], [5, 6]]
ragged_tensor = tf.ragged.constant(ragged_list)

# Create a dense tensor with the default value -1 for missing entries
dense_tensor = ragged_to_dense(ragged_tensor, default_value=-1)

print(dense_tensor.numpy())
