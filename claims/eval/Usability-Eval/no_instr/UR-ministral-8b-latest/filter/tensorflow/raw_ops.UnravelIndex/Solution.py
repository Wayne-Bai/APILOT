import tensorflow as tf

def get_coordinate_arrays(indices, shape):
    """
    Converts an array of flat indices into a tuple of coordinate arrays.

    Args:
    - indices: A 1-D array of flat indices.
    - shape: A tuple representing the shape of the input tensor.

    Returns:
    - A tuple containing coordinate arrays corresponding to the input flat indices.
    """
    # Calculate the shape slicing for each dimension
    coordinate_slices = [tf.slicing.slice(indices % i, 0, indices // (i - 1)) for i in shape]

    for i, slice_ in enumerate(coordinate_slices):
        if slice_.shape[0] % shape[i] != 0:
            size = (slice_.shape[0] // shape[i]) + 1
            new_slice = tf.pad(slice_, ((0, (size * shape[i]) - slice_.shape[0]),))
            coordinate_slices[i] = tf.split(new_slice, shape[i], axis=0)

    return tuple(coordinate_slices)

# Example usage
indices = tf.constant([3, 7, 10], dtype=tf.int32)
shape = (2, 3, 2)

coordinate_arrays = get_coordinate_arrays(indices, shape)
print(coordinate_arrays)
