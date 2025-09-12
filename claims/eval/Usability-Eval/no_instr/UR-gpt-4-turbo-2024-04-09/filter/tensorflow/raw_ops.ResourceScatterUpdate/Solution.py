import tensorflow as tf

def assign_sparse_updates(variable, indices, updates):
    """
    Function to assign sparse updates to a variable tensor using TensorFlow.

    Args:
    variable (tf.Variable): Tensorflow variable to update.
    indices (tf.Tensor): Tensor of type int32 or int64. Indices into the variable.
    updates (tf.Tensor): Tensor with the same type as 'variable'. Sparse updates to apply.

    Returns:
    tf.Tensor: Updated variable.
    """
    updated_variable = tf.tensor_scatter_nd_update(variable, indices, updates)
    return updated_variable

# Example usage:
variable = tf.Variable([[1, 2], [3, 4]], dtype=tf.float32)
indices = tf.constant([[0, 0], [1, 1]])
updates = tf.constant([10, 20], dtype=tf.float32)

updated_variable = assign_sparse_updates(variable, indices, updates)
print(updated_variable.numpy())
