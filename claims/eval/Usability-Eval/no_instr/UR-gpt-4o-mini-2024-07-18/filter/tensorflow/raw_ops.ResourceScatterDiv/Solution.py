import tensorflow as tf

def sparse_divide_updates(variable, sparse_updates, sparse_indices):
    """
    Divide sparse updates into the variable referenced by resource.

    Args:
    variable: A TensorFlow variable to be updated.
    sparse_updates: A tensor containing the sparse updates.
    sparse_indices: A tensor containing the indices of the updates.

    Returns:
    Updated variable after sparse division.
    """
    # Create a sparse tensor from the indices and updates
    sparse_tensor = tf.SparseTensor(indices=sparse_indices, values=sparse_updates, dense_shape=tf.shape(variable))

    # Instead of using outdated APIs, we can utilize tf.tensor_scatter_nd_update to apply the updates
    # Divide operations can be done in the form of tf.divide for elements that exist
    variable_value = tf.divide(variable, tf.sparse.to_dense(sparse_tensor, default_value=1.0))

    return variable_value

# Example usage:
var = tf.Variable(tf.random.uniform(shape=(3,), minval=1, maxval=10), dtype=tf.float32)
updates = tf.constant([2.0, 4.0])
indices = tf.constant([[0], [1]])

# Call the function to apply sparse division
updated_var = sparse_divide_updates(var, updates, indices)
print(updated_var.numpy())
