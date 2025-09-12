import tensorflow as tf

# Provided dimensions
original_shape = (1, 3, 3)
original_data = tf.ones(original_shape)

# Tiling dimensions
tile_shape = (2, 2, 2)  # Creating a 3x3 grid from 1x1 grid
repeated_data = tf.tile(original_data, tile_shape)

print("Original tensor:\n", original_data)
print("Tiled tensor:\n", repeated_data)
