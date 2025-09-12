import tensorflow as tf

def create_dense_tensor(ragged_tensor):
    """
    Create a dense tensor from a ragged tensor, altering its shape as needed.

    Parameters:
    - ragged_tensor (tf.RaggedTensor): The input ragged tensor.

    Returns:
    - tf.Tensor: The output dense tensor.
    """
    if ragged_tensor.shape.ndims > 2:
        raise ValueError("This function currently supports RaggedTensors with at most 2 dimensions.")

    # Create a dense tensor from the ragged tensor
    dense_tensor = tf.ragged.to_dense(ragged_tensor)

    return dense_tensor

# Example usage
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4], [5, 6, 7]])
dense_tensor = create_dense_tensor(ragged_tensor)

print(dense_tensor)
