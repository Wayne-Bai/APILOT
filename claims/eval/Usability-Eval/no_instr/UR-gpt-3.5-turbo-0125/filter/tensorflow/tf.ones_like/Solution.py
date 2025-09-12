
import tensorflow as tf

def ones_like(input_tensor):
    return tf.ones_like(input_tensor)

# Test
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
ones_tensor = ones_like(input_tensor)

print(ones_tensor)
