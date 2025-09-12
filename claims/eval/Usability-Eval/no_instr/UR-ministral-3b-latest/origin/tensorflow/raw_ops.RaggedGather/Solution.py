import tensorflow as tf

def gather_ragged_data(params, indices):
    """
    Gathers ragged slices from params axis 0 according to indices.

    Args:
        params (tf.Tensor): A `tf.RaggedTensor` with shape `[..., axis_0]`, where each row is a sequence.
        indices (tf.RaggedTensor): A `tf.RaggedTensor` with shape `[..., batch_size]`.

    Returns:
        tf.RaggedTensor: A `tf.RaggedTensor` containing the gathered slices.
    """

    # Use tf.raw_ops.gather_nd to gather from params along the non-redundant axis
    gathered_tensors = tf.raw_ops.gather_nd(params, [indices.flat[tf.newaxis, ...]])

    # Reshape and create the ragged tensor
    return tf.ragged.constant(gathered_tensors)

# Example usage:
params = tf.ragged.constant([
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
])

indices = tf.ragged.constant([0, 0, 1, 2, 0], row_splits=[0, 3, 7, 11])

gathered_data = gather_ragged_data(params, indices)
print(gathered_data)
