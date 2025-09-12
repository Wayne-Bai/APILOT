import tensorflow as tf

# Create a 2x2 matrix
matrix = tf.constant([[1, 2], [3, 4]])

# Tile the matrix twice in the vertical and horizontal directions
tiled_matrix = tf.tile(matrix, [2, 2])

# Print the tiled matrix
print(tiled_matrix)
