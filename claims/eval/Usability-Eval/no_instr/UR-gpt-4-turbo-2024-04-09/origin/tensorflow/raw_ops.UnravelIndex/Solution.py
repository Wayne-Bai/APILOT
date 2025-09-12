import tensorflow as tf

# Function to convert flat indices to coordinate arrays
def flat_indices_to_coordinates(indices, shape):
    return tf.raw_ops.UnravelIndex(indices=indices, dims=shape)

# Example usage
flat_indices = tf.constant([22, 41, 37], dtype=tf.int64)
shape = tf.constant([7, 6], dtype=tf.int64)
coordinate_arrays = flat_indices_to_coordinates(flat_indices, shape)
print(coordinate_arrays)
