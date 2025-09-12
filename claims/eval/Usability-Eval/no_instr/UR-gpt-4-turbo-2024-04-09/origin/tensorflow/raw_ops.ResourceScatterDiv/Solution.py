import tensorflow as tf

def divide_sparse_updates(resource, indices, updates):
    """
    Divides sparse updates into the variable referenced by the resource handle.

    Args:
    - resource (tf.Tensor): A handle to a tensor (typically a tf.Variable).
    - indices (tf.Tensor): A tensor of indices in the first dimension,
      these indicate the rows to be modified.
    - updates (tf.Tensor): Sparse updates to apply to the variable.

    Returns:
    - tf.Tensor: The updated variable.
    """
    # Ensuring the resource is a variable
    if not isinstance(resource, tf.Variable):
        raise ValueError("Resource must be a tensorflow Variable")

    # Data types check
    if not indices.dtype.is_integer:
        raise TypeError("Indices must be integers")
    if resource.dtype != updates.dtype:
        raise TypeError("The datatype of updates must be the same as that of the resource variable")

    # Shape and data compatibility validation
    resource_shape = tf.shape(resource)
    updates_shape = tf.shape(updates)
    tf.assert_equal(tf.size(indices), updates_shape[0], message="Length of indices must match the first dimension of updates")

    # Applying update
    resource.assign(tf.tensor_scatter_nd_div(resource, tf.expand_dims(indices, 1), updates))

    return resource

# Sample Usage:
v = tf.Variable([[1.0, 2.0], [3.0, 4.0]])
idx = tf.constant([0, 1])
upd = tf.constant([[5.0, 6.0], [7.0, 8.0]])

# Divide updates
result = divide_sparse_updates(v, idx, upd)
print(v.read_value())  # Output variable after updates
