import tensorflow as tf

# Define the tensor to be tiled
tensor = tf.constant([[1, 2], [3, 4]])

# Define the repetition factor for tiling
repetition = [2, 1]

# Tile the tensor
tiled_tensor = tf.tile(tensor, repetition)

# Print the result
print(tiled_tensor)
