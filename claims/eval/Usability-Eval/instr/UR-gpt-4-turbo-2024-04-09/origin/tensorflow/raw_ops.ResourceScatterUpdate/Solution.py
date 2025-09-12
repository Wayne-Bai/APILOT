import tensorflow as tf

def sparse_update_variable(resource, indices, updates, name=None):
    """
    Assigns sparse updates to the variable referenced by `resource`. The `indices` specify
    where to update in the variable and `updates` specify the new values to place.
    
    Args:
    resource (tf.Variable): The resource variable to update.
    indices (tf.Tensor): A tensor of indices in the variable to update.
    updates (tf.Tensor): Values to update in the specified indices of the variable.
    name (str): Optional name for the operation.
    
    Returns:
    tf.Operation: An operation that updates the variable.
    """
    return tf.raw_ops.ResourceScatterUpdate(resource=resource.handle, indices=indices, updates=updates, name=name)
