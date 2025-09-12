import tensorflow as tf

def convert_flat_indices_to_coordinates(flat_indices, shape):
    # Convert flat indices to coordinates
    coordinates = tf.unravel_index(flat_indices, shape)
    return coordinates

# Example usage:
flat_indices = tf.constant([0, 1, 2, 3, 4, 5])
shape = [2, 3]
coordinates = convert_flat_indices_to_coordinates(flat_indices, shape)
print(coordinates)
