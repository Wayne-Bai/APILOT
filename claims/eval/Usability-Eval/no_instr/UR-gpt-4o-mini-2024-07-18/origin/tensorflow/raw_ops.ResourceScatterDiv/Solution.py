import tensorflow as tf

def apply_sparse_updates(variable, indices, updates):
    """
    Applies sparse updates to a variable.

    Args:
        variable: A TensorFlow variable to update.
        indices: A tensor of indices where the updates are applied.
        updates: A tensor of updates to apply at the specified indices.
    
    Returns:
        The updated variable.
    """
    # Create a SparseTensor from indices and updates
    sparse_updates = tf.SparseTensor(indices, updates, tf.shape(variable))

    # Sparse update operation
    updated_variable = tf.tensor_scatter_nd_update(variable, indices, updates)

    return updated_variable

# Example usage
if __name__ == "__main__":
    # Create a variable
    var = tf.Variable([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)

    # Specify indices and updates
    indices = tf.constant([[0, 1], [1, 0]], dtype=tf.int64)
    updates = tf.constant([5.0, 6.0], dtype=tf.float32)

    # Apply sparse updates
    result = apply_sparse_updates(var, indices, updates)

    # Print the result
    tf.print("Updated variable:\n", result)
