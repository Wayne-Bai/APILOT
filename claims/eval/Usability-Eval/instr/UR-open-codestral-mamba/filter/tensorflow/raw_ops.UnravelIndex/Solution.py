import tensorflow as tf

# Define a tensor of indices
indices = tf.constant([[0, 2], [1, 1]])

# Calculate the shape of the indices tensor
shape = tf.shape(indices)

# Generate coordinate tensors
x_coords = tf.range(shape[0])
y_coords = tf.range(shape[1])

# Create coordinate pairs
coordinates = tf.meshgrid(x_coords, y_coords, indexing='ij')

# Print the coordinate pairs
print(coordinates)
