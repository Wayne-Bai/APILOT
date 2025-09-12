import tensorflow as tf

def convert_flat_indices_to_coordinates(flat_indices, shape):
    """
    Converts an array of flat indices into a tuple of coordinate arrays.

    Args:
    flat_indices: A 1-D Tensor of type int32 or int64. The flat indices to convert.
    shape: A 1-D Tensor of type int32 or int64. The shape of the tensor from which the indices are flattened.

    Returns:
    A tuple of Tensors, each of the same type as `flat_indices`. Each Tensor represents the coordinates
    corresponding to the flat indices.
    """
    # Convert flat indices to coordinates
    coordinates = tf.unravel_index(flat_indices, shape)
    
    return coordinates

# Example usage:
# flat_indices = tf.constant([0, 2, 3], dtype=tf.int32)
# shape = tf.constant([2, 2], dtype=tf.int32)
# coordinates = convert_flat_indices_to_coordinates(flat_indices, shape)
# print(coordinates)
