import tensorflow as tf

# Example method to create a custom gather operation
def tensorflow_gather(resource_name, indices):
    """
    Gather slices from the variable pointed to by resource according to indices.

    Args:
    - resource_name (str): Name of the resource in the variable.
    - indices (tensor): Indices to gather from the variable.

    Returns:
    - tf.Tensor: The gathered slices.
    """
    variable = tf.raw_ops.ResourceGather(name=resource_name, indices=indices)
    return variable

# Example usage
resource = tf.Variable([1, 2, 3, 4, 5], dtype=tf.int32)
indices = tf.constant([1, 3], dtype=tf.int32)
gather_result = tensorflow_gather(resource.name, indices)
print(gather_result)
