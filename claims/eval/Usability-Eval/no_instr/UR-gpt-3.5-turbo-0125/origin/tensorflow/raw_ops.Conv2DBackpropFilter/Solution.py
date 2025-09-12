
import tensorflow as tf

input = tf.constant([[1., 2., 3.],
                     [4., 5., 6.],
                     [7., 8., 9.],
                     [10., 11., 12.]], shape=[1, 4, 3, 1])

filter = tf.constant([[1., 0., -1.],
                      [2., 0., -2.],
                      [1., 0., -1.],
                      [1., 0., -1.]], shape=[4, 3, 1, 1])

grad = tf.raw_ops.Conv2DBackpropFilter(input=input, filter_sizes=[4, 3, 1, 1], out_backprop=input, strides=[1, 1, 1, 1], padding="VALID")

print(grad)
