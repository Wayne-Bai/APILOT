import tensorflow as tf

def transformelems(elems, fn):
    """
    Transforms elems by applying fn to each element unstacked on axis 0.

    Args:
    elems: A tensor with greater than or equal to 1 dimension.
    fn: A callable to be applied on each element of the tensor.

    Returns:
    A tensor with the same shape as elems and type resulting from applying fn.
    """
    # Get the number of dimensions in elems
    num_dims = len(elems.shape)

    # Unstack elems along axis 0
    unstacked_elems = tf.unstack(elems, axis=0)

    # Apply fn on each element
    transformed_elems = [fn(elem) for elem in unstacked_elems]

    # Stack transformed_elems back to the original shape
    transformed_elems = tf.stack(transformed_elems, axis=0)

    # Set the shape explicitly
    transformed_elems = tf.reshape(transformed_elems, shape=elems.shape)

    return transformed_elems

# Example usage:
elems = tf.constant([[1, 2], [3, 4]])
fn = lambda x: x * 2

transformed_elems = transformelems(elems, fn)
print(transformed_elems)
