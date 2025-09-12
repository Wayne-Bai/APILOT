import tensorflow as tf

def indices_to_coordinates(indices, shape):
    """
    Convert an array of flat indices into a tuple of coordinate arrays.
    
    Args:
        indices: A 1-D Tensor of flat indices.
        shape: A 1-D Tensor or a list that represents the shape of the array.

    Returns:
        A tuple of Tensors, where each Tensor corresponds to a dimension 
        and contains the coordinates for that dimension.
    """
    return tf.experimental.numpy.unravel_index(indices, shape)

# Example usage:
indices = tf.constant([0, 1, 2, 3, 4])
shape = tf.constant([2, 3])  # Example shape of a 2D array

coordinates = indices_to_coordinates(indices, shape)
print(coordinates)
