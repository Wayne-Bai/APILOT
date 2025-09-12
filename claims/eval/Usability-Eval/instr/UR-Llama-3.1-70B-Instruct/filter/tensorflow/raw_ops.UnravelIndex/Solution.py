# Import necessary libraries
import tensorflow as tf

# Define a function to convert flat indices into a tuple of coordinate arrays
def convert_flat_indices(indices, shape):
    """
    Converts an array of flat indices into a tuple of coordinate arrays.

    Args:
        indices: A 1-D tensor of flat indices.
        shape: The shape of the original array.

    Returns:
        A tuple of coordinate arrays.
    """
    return tf.raw_ops.ScatterNd(indices=indices, shape=shape, updates=tf.ones_like(indices, dtype=indices.dtype))

# Test the function
indices = tf.constant([1, 4, 9, 16])
shape = tf.constant([5, 5])

output = convert_flat_indices(indices, shape)
print(output)
