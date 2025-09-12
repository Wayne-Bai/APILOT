import tensorflow as tf

def convolution_2d(inputs, filters, kernel_size, strides, padding):
    return tf.nn.conv2d(inputs, filters, strides, padding)
