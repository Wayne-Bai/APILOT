import tensorflow as tf

def sparse_divide(variable, indices, updates):
    """
    Applies sparse division to the variable using the provided indices and updates.
    `variable` is a TensorFlow Variable.
    `indices` is the index locations that will be updated.
    `updates` are the values that will be used for performing division at the specified indices.

    Args:
        variable (tf.Variable): Tensor to be updated.
        indices (tf.Tensor or any appropriate format recognized by TensorFlow for indices): Indices for the sparse update.
        updates (tf.Tensor): Values to use for the updates.

    Returns:
        None, updates the TensorFlow variable in place.
    """
    # Ensure the updates can be broadcast to the shape at the indices
    reshaped_updates = tf.reshape(updates, [-1] + [1] * (variable.shape.ndims - 1))

    # Create a tensor of the same shape as `variable`, with zeros everywhere except where specified by `indices`
    delta = tf.scatter_nd(indices, reshaped_updates, variable.shape)

    # Divide the variable by the delta tensor using the tf.divide function, which safely handles division by zero
    # and broadcasts appropriately.
    variable.assign(tf.divide(variable, tf.where(delta != 0, delta, 1)))

# Example usage:
variable = tf.Variable([[6.0, 9.0], [12.0, 15.0]])
indices = tf.constant([[0, 0], [1, 1]])
updates = tf.constant([2.0, 3.0])

# Apply sparse division operation
sparse_divide(variable, indices, updates)

# Print the updated variable to check results
tf.print(variable)
