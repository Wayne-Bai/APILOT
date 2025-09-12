
import tensorflow as tf

@tf.function
def compute_maxpool_gradients(input, gradient, argmax, ksize, strides, padding, data_format='NHWC'):
    return tf.raw_ops.MaxPoolGrad(
        orig_input=input,
        orig_output=gradient,
        grad=argmax,
        ksize=ksize,
        strides=strides,
        padding=padding,
        data_format=data_format
    )

# Example usage
input = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
gradient = tf.constant([[1.0, 0.5], [0.3, 0.8]])
argmax = tf.constant([[0, 2], [1, 0]])
ksize = [1, 2, 2, 1]
strides = [1, 2, 2, 1]
padding = 'VALID'

result = compute_maxpool_gradients(input, gradient, argmax, ksize, strides, padding)
print(result)
