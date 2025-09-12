import tensorflow as tf

def sparse_update_variable(resource, indices, updates):
    # Ensure the resource is a variable
    if not isinstance(resource, tf.Variable):
        raise ValueError("The resource must be a tf.Variable.")

    # Create a mask for the updates
    mask = tf.scatter_nd(indices, tf.ones_like(updates), tf.shape(resource))

    # Apply the updates
    updated_resource = tf.where(mask > 0, updates, resource)

    # Assign the updated values back to the resource
    resource.assign(updated_resource)

# Example usage:
# Assuming 'variable' is a tf.Variable and 'indices' and 'updates' are tensors
# variable = tf.Variable([1.0, 2.0, 3.0, 4.0])
# indices = tf.constant([[1], [3]])
# updates = tf.constant([9.0, 10.0])
# sparse_update_variable(variable, indices, updates)
