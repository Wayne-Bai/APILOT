import tensorflow as tf

# Example tensor
tensor = tf.constant([[1, 2],
                      [3, 4]])

# Tiling multiples (e.g., 2 times)
multiples = tf.constant([2, 2])

# Tiling the tensor
tiled_tensor = tf.tile(tensor, multiples)

# Printing the tiled tensor
print(tiled_tensor)
