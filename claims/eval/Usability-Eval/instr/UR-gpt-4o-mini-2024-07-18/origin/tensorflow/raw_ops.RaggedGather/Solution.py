import tensorflow as tf

def gather_ragged_slices(params, indices):
    """
    Gather ragged slices from params according to indices along axis 0.

    Args:
    params: A RaggedTensor to gather slices from.
    indices: A tensor containing the indices of the slices to gather.

    Returns:
    A RaggedTensor containing the gathered slices.
    """
    # Convert the params to RaggedTensor if not already
    if not isinstance(params, tf.RaggedTensor):
        params = tf.RaggedTensor.from_tensor(params)

    # Indexing directly from the RaggedTensor
    gathered = tf.ragged.boolean_mask(params, tf.expand_dims(tf.range(tf.shape(params)[0]), axis=1) == indices)

    return gathered

# Example usage
if __name__ == "__main__":
    # Define a RaggedTensor
    values = [[1, 2], [3, 4, 5], [6]]
    row_splits = [0, 2, 5, 6]
    ragged_tensor = tf.RaggedTensor.from_row_splits(values, row_splits)

    # Define indices to gather
    indices = tf.constant([0, 1])

    # Gather ragged slices
    result = gather_ragged_slices(ragged_tensor, indices)
    print(result)
