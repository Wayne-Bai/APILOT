import tensorflow as tf

def scatter_div_example():
    # Create a variable tensor
    variable = tf.Variable([[10.0, 20.0], [30.0, 40.0]], dtype=tf.float32)

    # Indices where updates should be applied
    indices = tf.constant([0, 1], dtype=tf.int32)

    # Sparse updates that we want to divide into the variable tensor
    updates = tf.constant([[2.0, 4.0], [3.0, 5.0]], dtype=tf.float32)

    # Gather the existing values using the indices to perform the division
    gathered = tf.gather(variable, indices)

    # Perform the division
    divided_values = gathered / updates

    # Use tf.tensor_scatter_nd_update to update the variable
    updated_variable = tf.tensor_scatter_nd_update(variable, tf.expand_dims(indices, 1), divided_values)

    return updated_variable

# Example usage
updated_value = scatter_div_example()
print("Updated Tensor:")
print(updated_value.numpy())
