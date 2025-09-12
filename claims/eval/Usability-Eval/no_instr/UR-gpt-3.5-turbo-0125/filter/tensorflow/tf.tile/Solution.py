
import tensorflow as tf

def tile_tensor(input_tensor, multiples):
    tiled_tensor = tf.tile(input_tensor, multiples)
    return tiled_tensor

# Example usage
input_tensor = tf.constant([[1, 2], [3, 4]])
multiples = [2, 3]
tiled_result = tile_tensor(input_tensor, multiples)

with tf.Session() as sess:
    result = sess.run(tiled_result)
    print(result)
