import tensorflow as tf

# Define the input tensor shape (batch_size, height, width, channels)
input_shape = (1, 5, 5, 1)
input_tensor = tf.constant([[[[1.0], [2.0], [3.0], [4.0], [5.0]],
                             [[6.0], [7.0], [8.0], [9.0], [10.0]],
                             [[11.0], [12.0], [13.0], [14.0], [15.0]],
                             [[16.0], [17.0], [18.0], [19.0], [20.0]],
                             [[21.0], [22.0], [23.0], [24.0], [25.0]]]], shape=input_shape)

# Define the filter/kernel shape (filter_height, filter_width, in_channels, out_channels)
filter_shape = (3, 3, 1, 1)
filter_tensor = tf.constant([[[[1.0]], [[0.0]], [[-1.0]]],
                             [[[1.0]], [[0.0]], [[-1.0]]],
                             [[[1.0]], [[0.0]], [[-1.0]]]], shape=filter_shape)

# Define the gradient with respect to the output of the convolution
output_grad = tf.constant([[[[1.0], [1.0], [1.0]], 
                            [[1.0], [1.0], [1.0]], 
                            [[1.0], [1.0], [1.0]]]], shape=(1, 3, 3, 1))

# Calculate padding and strides
strides = [1, 1, 1, 1]
padding = 'VALID'

# Compute the gradients of the input
# Create a Conv2D layer
conv_layer = tf.nn.conv2d(input=input_tensor, filters=filter_tensor, strides=strides, padding=padding)

# Use tf.gradients to compute the gradient of the input tensor
input_grad = tf.gradients(conv_layer, input_tensor, grad_ys=output_grad)

# Execute the computation graph to get the result
with tf.Session() as sess:
    input_grad_result = sess.run(input_grad)
    print("Gradient with respect to the input tensor:")
    print(input_grad_result)
