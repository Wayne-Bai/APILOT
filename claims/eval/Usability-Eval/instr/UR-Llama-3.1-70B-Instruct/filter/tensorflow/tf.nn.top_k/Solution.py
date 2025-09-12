import tensorflow as tf

def find_k_largest(tensor, k):
    """
    Finds values and indices of the k largest entries for the last dimension.

    Args:
        tensor: Input tensor.
        k: Number of largest entries to find.

    Returns:
        values: Tensor with the k largest values.
        indices: Tensor with the indices of the k largest values.
    """
    # Get the shape of the input tensor
    shape = tf.shape(tensor)

    # Reshape the tensor to 2D for easier manipulation
    flattened_tensor = tf.reshape(tensor, (-1, shape[-1]))

    # Find the indices of the k largest values along the last dimension
    _, indices = tf.nn.top_k(flattened_tensor, k, sorted=True)

    # Gather the k largest values from the flattened tensor
    values = tf.gather(flattened_tensor, indices, batch_dims=1)

    return values, indices

# Example usage:
tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k = 2

values, indices = find_k_largest(tensor, k)
print("Values:", values)
print("Indices:", indices)
