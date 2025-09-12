import tensorflow as tf

def tile_tensor(tensor, multiples):
    return tf.tile(tensor, multiples)

# Example usage:
tensor = tf.constant([[1, 2], [3, 4]])
multiples = [2, 3]
result = tile_tensor(tensor, multiples)
print(result)
