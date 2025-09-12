import tensorflow as tf

def gradient_of_convolution(input, filter):
    # Use the TensorFlow API to compute the gradient of the convolution with respect to the input
    return tf.gradients(tf.nn.conv2d(input, filter), input)
