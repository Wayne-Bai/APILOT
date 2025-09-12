import tensorflow as tf

# Define the input tensor, filter/kernel, and gradients
input_shape = (1, 5, 5, 1)  # Example input shape, batch_size x height x width x channels
kernel_shape = (3, 3, 1, 1) # Example filter shape, filter_height x filter_width x in_channels x out_channels
strides = [1, 1, 1, 1]   # Stride of the sliding window for each dimension of input
padding = 'SAME'         # Padding method used for the convolution

# Simulate some input data and kernels
input_tensor = tf.constant([[[[1], [2], [3], [4], [5]],
                             [[6], [7], [8], [9], [10]],
                             [[11], [12], [13], [14], [15]],
                             [[16], [17], [18], [19], [20]],
                             [[21], [22], [23], [24], [25]]]], dtype=tf.float32)
filter_kernel = tf.constant([[[[1]], [[0]], [[-1]]],
                             [[[1]], [[0]], [[-1]]],
                             [[[1]], [[0]], [[-1]]]], dtype=tf.float32)
dy = tf.ones((1, 5, 5, 1), dtype=tf.float32)  # Simulate some gradients

# Perform the convolution
conv_output = tf.nn.conv2d(input_tensor, filter_kernel, strides=strides, padding=padding)

# Manual computation of the gradients with respect to the input
input_grad = tf.nn.conv2d_backprop_input(
    input_shape=input_shape,
    filter=filter_kernel,
    out_backprop=dy,
    strides=strides,
    padding=padding
)

# Display the original convolution output and the computed gradient
tf.print("Convolution Output:\n", conv_output)
tf.print("Gradient w.r.t. Input:\n", input_grad)
