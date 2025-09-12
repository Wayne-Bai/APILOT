import tensorflow as tf

def sparse_divide(resource, indices, updates):
    """
    Divides sparse updates into the variable referenced by resource.
    
    Args:
    resource (tf.Tensor): A resource handle to the variable to be updated.
    indices (tf.Tensor): A tensor of indices into the first dimension of `resource`.
    updates (tf.Tensor): A tensor of values that will be used for division.
    
    Returns:
    tf.Operation: The operation that performs the divisive update.
    """
    # Obtain a read handle to the current variables
    var_data = tf.gather(resource, indices)
    
    # Divide the updates
    new_values = tf.divide(var_data, updates)
    
    # Scatter the new values back into the original variable
    return tf.tensor_scatter_nd_update(resource, tf.expand_dims(indices, 1), new_values)

# Example usage:
# Assuming `resource` is a TensorFlow variable created beforehand,
# `indices` is the indices to update, and `updates` are the values for updates.
resource = tf.Variable([10.0, 20.0, 30.0, 40.0])
indices = tf.constant([1, 3])
updates = tf.constant([2.0, 4.0])
update_operation = sparse_divide(resource, indices, updates)

# To apply the updates
tf.compat.v1.global_variables_initializer()
with tf.compat.v1.Session() as sess:
    sess.run(update_operation)
    print(sess.run(resource))
