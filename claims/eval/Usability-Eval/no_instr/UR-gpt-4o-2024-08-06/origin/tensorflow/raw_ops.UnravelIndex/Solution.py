import tensorflow as tf

# Convert flat indices to coordinates
def flat_to_coordinates(flat_indices, shape):
    # Convert flat indices to coordinates using tf.unravel_index
    coordinates = tf.unravel_index(flat_indices, shape)
    return coordinates

# Example usage
flat_indices = tf.constant([2, 5, 7])
shape = (3, 3)
coordinates = flat_to_coordinates(flat_indices, shape)

# Result
print("Flat indices:", flat_indices.numpy())
print("Coordinates:", [coord.numpy() for coord in coordinates])
