
import tensorflow as tf

def convert_flat_indices(flat_indices):
    """
    Converts an array of flat indices into a tuple of coordinate arrays.

    Args:
        flat_indices: A 1-D Tensor with type int32 or int64. The flat indices for the conversion.

    Returns:
        A tuple of two 1-D Tensors, each with type int32 or int64, representing the coordinate arrays of the input flat indices.
    """
    # Use tf.range to generate a range of integers corresponding to the number of dimensions in the input array
    num_dims = tf.size(flat_indices)
    dim_ranges = [tf.range(0, num_dims)] * 2

    # Use tf.unravel_index to convert the flat indices to coordinate arrays
    coord_arrays = tf.map_fn(lambda x: tf.unravel_index(x, dim_ranges), flat_indices)

    return coord_arrays
