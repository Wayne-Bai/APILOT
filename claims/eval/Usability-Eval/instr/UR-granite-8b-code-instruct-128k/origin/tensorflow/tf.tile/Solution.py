import tensorflow as tf

# Create a 2x2 matrix
matrix = tf.constant([[1, 2], [3, 4]])

# Tile the matrix 2 times in the vertical and 3 times in the horizontal direction
tiled_matrix = tf.tile(matrix, [2, 3])

# Print the tiled matrix
print(tiled_matrix)
