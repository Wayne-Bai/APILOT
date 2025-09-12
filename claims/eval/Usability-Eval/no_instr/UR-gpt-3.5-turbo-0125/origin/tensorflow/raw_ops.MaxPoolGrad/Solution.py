
import tensorflow as tf

@tf.function
def maxpool_gradient(input, grad, ksize, strides, padding, data_format='NHWC', name=None):
    with tf.GradientTape() as tape:
        tape.watch(input)
        output = tf.nn.max_pool(input, ksize=ksize, strides=strides, padding=padding, data_format=data_format, name=name)
    return tape.gradient(output, input, output_gradients=grad)

input = tf.constant([[[[1.0], [2.0], [1.0], [0.0]],
                      [[0.0], [1.0], [2.0], [1.0]],
                      [[2.0], [0.0], [1.0], [2.0]],
                      [[1.0], [2.0], [0.0], [1.0]]]], dtype=tf.float32)

grad = tf.constant([[[[1.0], [2.0]],
                     [[0.0], [1.0]]]], dtype=tf.float32)

ksize = [1, 2, 2, 1]
strides = [1, 1, 1, 1]
padding = 'VALID'

result = maxpool_gradient(input, grad, ksize, strides, padding)
print(result)
