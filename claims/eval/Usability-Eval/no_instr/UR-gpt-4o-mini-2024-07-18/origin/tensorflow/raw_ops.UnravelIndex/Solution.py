import tensorflow as tf

def convert_flat_indices_to_coordinates(indices, shape):
    # Convert flat indices to coordinates
    coordinates = tf.experimental.numpy.unravel_index(indices, shape)
    return coordinates

# Example usage
flat_indices = tf.constant([0, 1, 2, 3, 4])
shape = (2, 2, 2)
coordinates = convert_flat_indices_to_coordinates(flat_indices, shape)

print("Coordinates:", coordinates)
