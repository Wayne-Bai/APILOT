
import tensorflow as tf

# Define the input and output shapes for the layer
input_shape = (28, 28, 1)
output_shape = (24, 24, 32)

# Define the filter shape and its stride
filter_shape = (5, 5, 1, 32)
stride = (1, 1)

# Define the padding type and pad value
padding = 'VALID'
pad_value = 0.0

# Compute the convolutional layer using raw ops
convolution = tf.raw_ops.Conv2D(
    input=input_shape, output=output_shape, filter=filter_shape, stride=stride, padding=padding, pad_value=pad_value)

# Compute the gradients of the convolutional layer with respect to the weights
weights = tf.Variable(tf.random_normal(convolution.filter))
gradients = tf.raw_ops.Conv2DGrad(
    input=input_shape, filter=weights, stride=stride, padding=padding)
