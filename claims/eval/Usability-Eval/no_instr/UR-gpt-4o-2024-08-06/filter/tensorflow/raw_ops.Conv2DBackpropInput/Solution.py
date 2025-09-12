import tensorflow as tf

# Define the input tensor
input_tensor = tf.random.normal([1, 5, 5, 1])  # Shape: [batch, height, width, channels]

# Define a filter/kernel tensor
filter_tensor = tf.random.normal([3, 3, 1, 1])  # Shape: [filter_height, filter_width, input_channels, output_channels]

# Define a 4D tensor with the same dimensions as the output of a convolution
out_backprop = tf.random.normal([1, 5, 5, 1])  # Shape: [batch, out_height, out_width, out_channels]

# Define the strides and padding type for the convolution
strides = [1, 1, 1, 1]
padding = 'SAME'

# Calculate the input gradient using the gradients of the convolution with respect to the input
input_gradients = tf.nn.conv2d_backprop_input(
    input_sizes=tf.shape(input_tensor),
    filter=filter_tensor,
    out_backprop=out_backprop,
    strides=strides,
    padding=padding
)

# Print the computed input gradients tensor
tf.print("Input Gradients: ", input_gradients)
