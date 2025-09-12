import tensorflow as tf

def divide_sparse_updates(resource, indices, updates):
    """
    Divides sparse updates into the variable referenced by resource.

    Parameters:
    - resource: A handle to the variable to update. This tensor must be of type Resource.
    - indices: A tensor of indices in the first dimension of the variable where updates are to be applied.
    - updates: A tensor of values that will be used for division at corresponding indices.

    Returns:
    Updated tensor after performing sparse division.
    """
    # To perform the sparse divide, we first gather the original values from the resource
    # at the specified indices.
    original_values = tf.gather(resource, indices)
    
    # Perform division of original values by the updates
    new_values = tf.divide(original_values, updates)
    
    # Use scatter update to place the divided results back to the variable
    return tf.tensor_scatter_nd_update(resource, tf.expand_dims(indices, 1), new_values)

# Example of usage
# Create a resource variable
variable = tf.Variable([10.0, 20.0, 30.0, 40.0, 50.0])

# Define indices and updates
indices = tf.constant([0, 2, 4])
updates = tf.constant([2.0, 3.0, 5.0])

# Perform division
result_variable = divide_sparse_updates(variable, indices, updates)

# Initialize the variable and print result
init_op = tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session() as sess:
    sess.run(init_op)
    print(sess.run(result_variable))
