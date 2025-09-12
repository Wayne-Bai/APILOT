import tensorflow as tf
import numpy as np

def convert_indices_to_coordinates(indices, shape):
    """
    Converts an array of flat indices into a tuple of coordinate arrays.

    Args:
    indices: A Tensor. Must be one of the following types: int32, int64.
    shape: A Tensor. Must have the same dtype as indices. 1-D. The shape of the array to use for unraveling indices.

    Returns:
    A tuple of Tensor objects with the same shape as the given shape and same dtype as indices.
    """
    # Convert indices to a TensorFlow tensor
    indices = tf.constant(indices, dtype=tf.int64)
    shape = tf.constant(shape, dtype=tf.int64)

    coords = []
    for dim in reversed(shape.numpy()):
        coords.append(indices % dim)
        indices = indices // dim
    return tuple(reversed(coords))

# Test the function
indices = np.array([60, 45, 36], dtype=np.int64)
shape = np.array([10, 7, 6], dtype=np.int64)
print(convert_indices_to_coordinates(indices, shape))
