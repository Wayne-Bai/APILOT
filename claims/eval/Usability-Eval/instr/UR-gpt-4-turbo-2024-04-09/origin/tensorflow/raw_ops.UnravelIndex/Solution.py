import tensorflow as tf

# Function to convert flat indices to coordinate arrays using tf.raw_ops
def flat_indices_to_coordinates(flat_indices, shape):
    return tf.raw_ops.FlatCoordinates(indices=flat_indices, shape=shape)

# Example usage:
shape = [10, 20, 30]  # Define the tensor shape
flat_indices = [115, 235, 1234]  # Example of flat indices
coordinates = flat_indices_to_coordinates(flat_indices=flat_indices, shape=shape)

print("Coordinates:", coordinates)
