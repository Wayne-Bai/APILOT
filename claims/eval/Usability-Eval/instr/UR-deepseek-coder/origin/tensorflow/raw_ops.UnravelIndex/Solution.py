import tensorflow as tf

def convert_flat_indices_to_coordinates(flat_indices, shape):
    """
    Converts an array of flat indices into a tuple of coordinate arrays.

    Args:
    flat_indices: A Tensor of type int32. 1-D. Indices into the flattened version of a tensor of dimensions shape.
    shape: A Tensor of type int32. 1-D. Shape of the tensor into which the indices point.

    Returns:
    A tuple of Tensors, each of type int32. The tuple contains len(shape) tensors.
    """
    coordinates = tf.unravel_index(flat_indices, shape)
    return coordinates

# Example usage:
flat_indices = tf.constant([0, 1, 2, 3], dtype=tf.int32)
shape = tf.constant([2, 2], dtype=tf.int32)

coordinates = convert_flat_indices_to_coordinates(flat_indices, shape)
print(coordinates)
