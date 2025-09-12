# Importing the necessary libraries
import tensorflow as tf

# Creating a tensor of flat indices
flat_indices = tf.constant([2, 4, 3, 5, 7])

# Specifying the shape of the output tensor
output_shape = [3, 3]

# Using tf.unravel_index to get the coordinate arrays
coordinate_arrays = tf.unravel_index(flat_indices, output_shape)

# Printing the coordinate arrays
print("Coordinate arrays: ", coordinate_arrays)
