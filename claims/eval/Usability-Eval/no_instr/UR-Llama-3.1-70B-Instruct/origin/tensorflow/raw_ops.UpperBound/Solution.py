import tensorflow as tf

def apply_upper_bound(sorted_search_values, values):
    """
    Applies upper_bound(sorted_search_values, values) along each row.

    Args:
    sorted_search_values (tf.Tensor): A 2D tensor with sorted values along the last dimension.
    values (tf.Tensor): A 2D tensor with values to search for.

    Returns:
    tf.Tensor: A 2D tensor with indices of the upper bound for each value in the sorted_search_values.
    """

    # Get the number of rows in the input tensors
    num_rows = tf.shape(sorted_search_values)[0]

    # Reshape the values tensor to a 1D tensor
    values_reshaped = tf.reshape(values, [-1])

    # Tile the sorted_search_values tensor to match the size of the values tensor
    sorted_search_values_tiled = tf.tile(tf.expand_dims(sorted_search_values, 1), [1, tf.shape(values)[1], 1])

    # Reshape the tiled tensor to match the size of the values tensor
    sorted_search_values_reshaped = tf.reshape(sorted_search_values_tiled, [-1, tf.shape(sorted_search_values)[1]])

    # Use tf.searchsorted to find the upper bound for each value in the sorted_search_values
    indices = tf.searchsorted(sorted_search_values_reshaped, values_reshaped, side='right')

    # Reshape the indices tensor to match the original shape of the values tensor
    indices_reshaped = tf.reshape(indices, [num_rows, tf.shape(values)[1]])

    return indices_reshaped


# Example usage
sorted_search_values = tf.constant([[1, 3, 5, 7], [2, 4, 6, 8]])
values = tf.constant([[3, 4], [5, 6]])

result = apply_upper_bound(sorted_search_values, values)
print(result)
