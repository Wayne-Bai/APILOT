import tensorflow as tf

# Define the tensor for which we want to generate the coordinate arrays
input_array = tf.constant([1, 2, 3, 4, 5])

# Define the indices
indices = tf.constant([0, 2, 4])

# Convert indices to tuple of coordinate arrays
coordinate_arrays = tf.gather_nd(tf.range(tf.size(input_array)), indices)

print("Original array: ", input_array.numpy())
print("Indices: ", indices.numpy())
print("Coordinate arrays: ", coordinate_arrays.numpy())
