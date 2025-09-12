import tensorflow as tf

# Function to convert flat indices to coordinate arrays
def flat_indices_to_coordinates(flat_indices, dims):
    coordinates = tf.experimental.numpy.unravel_index(flat_indices, dims)
    return coordinates

# Example usage
flat_indices = tf.constant([0, 1, 2, 10, 20])
dims = (5, 5)  # Assuming a 5x5 array
coordinates = flat_indices_to_coordinates(flat_indices, dims)

print(coordinates)
