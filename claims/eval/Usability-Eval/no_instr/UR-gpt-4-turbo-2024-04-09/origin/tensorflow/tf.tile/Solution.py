import tensorflow as tf

def tile_tensor(input_tensor, multiples):
    return tf.tile(input_tensor, multiples)

# Example usage:
input_tensor = tf.constant([[1, 2], [3, 4]])
multiples = [2, 3]  # Specify tiling configuration

tiled_tensor = tile_tensor(input_tensor, multiples)
print(tiled_tensor)
