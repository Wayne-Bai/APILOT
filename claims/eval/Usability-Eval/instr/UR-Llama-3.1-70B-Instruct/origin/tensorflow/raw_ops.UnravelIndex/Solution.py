import tensorflow as tf

# Create a tensor with flat indices
flat_indices = tf.constant([2, 4, 6, 8])

# Define the shape to which the indices should be unraveled.
shape = tf.constant([16, 8, 8])

# Use the tf.unravel_index function to convert flat indices to coordinate arrays
coordinate_arrays = tf.unravel_index(flat_indices, shape)

print(coordinate_arrays)

# To get the actual coordinates, use the following
for coordinate in tf.split(coordinate_arrays, len(shape)):
    print(coordinate)
