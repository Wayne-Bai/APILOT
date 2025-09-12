import tensorflow as tf

# Define the input tensor and its shape
input_tensor = tf.constant([[[[1.0], [2.0]], [[3.0], [4.0]]]], dtype=tf.float32)
input_shape = tf.shape(input_tensor)

# Define the filter size, strides and padding
ksize = [1, 2, 2, 1]
strides = [1, 1, 1, 1]
padding = 'VALID'

# Perform max pooling operation
maxpool_output = tf.nn.max_pool2d(input_tensor, ksize=ksize, strides=strides, padding=padding)

# Compute the gradient of the maxpooling backprop
maxpool_grad = tf.raw_ops.MaxPoolGrad(
    orig_input=input_tensor,
    orig_output=maxpool_output,
    grad=tf.constant([[[[1.0]]]], dtype=tf.float32), # Example gradient, same shape as maxpool output
    ksize=ksize,
    strides=strides,
    padding=padding
)

# To print or use the computed gradients
tf.print("Input Tensor:", input_tensor)
tf.print("MaxPool Output:", maxpool_output)
tf.print("MaxPool Gradients:", maxpool_grad)
