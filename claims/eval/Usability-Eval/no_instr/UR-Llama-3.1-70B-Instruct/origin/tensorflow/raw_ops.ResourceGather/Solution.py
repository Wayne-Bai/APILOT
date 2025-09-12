import tensorflow as tf

def gather_slices(resource, indices, validation_string=None, name=None):
    """
    Gather slices from the variable pointed to by resource according to indices.

    Args:
        resource: A handle to the resource.
        indices: A 0/1-D integer Tensor. The indices to gather.
        validation_string: An optional string. Defaults to None.
        name: A name for the operation (optional).

    Returns:
        A Tensor. Has the same type as resource.
    """
    with tf.name_scope(name or "gather_slices"):
        return tf.raw_ops.ResourceGather(resource=resource,
                                         indices=indices,
                                         validation_string=validation_string,
                                         name=name)

# Example usage
if __name__ == "__main__":
    # Create a tf variable
    var = tf.Variable([[1, 2, 3], [4, 5, 6]], dtype=tf.float32)

    # Get the resource handle
    resource = var.handle

    # Define the indices to gather
    indices = tf.constant([0, 1])

    # Gather slices
    gathered = gather_slices(resource, indices)

    with tf.Session() as sess:
        sess.run(var.initializer)
        print(sess.run(gathered))
