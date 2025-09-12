import tensorflow as tf

def convert_flat_indices_to_coordinates(flat_indices, shape):
    """Converts an array of flat indices into a tuple of coordinate arrays."""
    indices = tf.retmap_func(flat_indices, np.arange(shape[0]), axis=0)

