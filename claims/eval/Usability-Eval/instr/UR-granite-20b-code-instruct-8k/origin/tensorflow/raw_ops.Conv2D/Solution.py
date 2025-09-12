import tensorflow as tf

def conv2d(input, filter, strides, padding):
    return tf.nn.conv2d(input, filter, strides, padding)
