import tensorflow as tf

def conv2d_filter_gradient(input_tensor, filter_tensor, grad_output, strides, padding):
    # Compute the gradients of the convolution with respect to the filter
    grad_filter = tf.nn.conv2d_backprop_filter(
        input=input_tensor,
        filter_sizes=filter_tensor.shape,
        out_backprop=grad_output,
        strides=strides,
        padding=padding
    )
    return grad_filter

# Example usage:
# input_tensor: [batch_size, height, width, channels_in]
# filter_tensor: [filter_height, filter_width, channels_in, channels_out]
# grad_output: [batch_size, out_height, out_width, channels_out]
# strides: [1, stride_height, stride_width, 1]
# padding: 'SAME' or 'VALID'

input_tensor = tf.random.normal([10, 32, 32, 3])
filter_tensor = tf.random.normal([5, 5, 3, 16])
grad_output = tf.random.normal([10, 32, 32, 16])
strides = [1, 1, 1, 1]
padding = 'SAME'

grad_filter = conv2d_filter_gradient(input_tensor, filter_tensor, grad_output, strides, padding)
print(grad_filter)
