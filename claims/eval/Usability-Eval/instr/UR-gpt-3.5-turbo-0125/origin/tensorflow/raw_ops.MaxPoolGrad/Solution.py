
import tensorflow as tf

@tf.function
def maxpool_grad(input, output, grad, ksize, strides, padding):
    return tf.nn.max_pool_gradV2(input, output, grad, ksize=ksize, strides=strides, padding=padding)

# Example usage:
input = tf.constant([[1.0, 2.0, 3.0, 4.0],
                     [5.0, 6.0, 7.0, 8.0],
                     [9.0, 10.0, 11.0, 12.0],
                     [13.0, 14.0, 15.0, 16.0]], dtype=tf.float32)
output = tf.nn.max_pool(input, ksize=(2, 2), strides=(2, 2), padding='VALID')
grad = tf.constant([[1.0, 2.0],
                    [3.0, 4.0]], dtype=tf.float32)
ksize = [1, 2, 2, 1]
strides = [1, 2, 2, 1]
padding = b'VALID'

result = maxpool_grad(input, output, grad, ksize, strides, padding)
print(result)
