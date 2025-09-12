import tensorflow as tf

def conv2d_filter_grad(input_tensor, filter_tensor, grad, strides, padding, data_format='NHWC', dilations=None):
    """
    Computes the gradients of convolution with respect to the filter.

    Args:
        input_tensor: A 4D Tensor of shape [batch, in_height, in_width, in_channels].
        filter_tensor: A 4D Tensor of shape [filter_height, filter_width, in_channels, out_channels].
        grad: A 4D Tensor of shape [batch, out_height, out_width, out_channels].
        strides: A list of ints that has length >= 4. The stride of the sliding window for each dimension of input.
        padding: A string from: "SAME", "VALID". The type of padding algorithm to use.
        data_format: An optional string from: "NHWC", "NCHW". Defaults to "NHWC".
        dilations: An optional list of ints. Defaults to [1, 1, 1, 1]. The dilation rate to use for dilated convolution.

    Returns:
        A 4D Tensor of shape [filter_height, filter_width, in_channels, out_channels].
    """
    if dilations is None:
        dilations = [1, 1, 1, 1]

    # Ensure the data format is consistent
    if data_format == 'NHWC':
        data_format_tf = 'NHWC'
    elif data_format == 'NCHW':
        data_format_tf = 'NCHW'
    else:
        raise ValueError("data_format must be either 'NHWC' or 'NCHW'")

    # Compute the gradient with respect to the filter
    filter_grad = tf.nn.conv2d_backprop_filter(
        input=input_tensor,
        filter_sizes=filter_tensor.shape,
        out_backprop=grad,
        strides=strides,
        padding=padding,
        data_format=data_format_tf,
        dilations=dilations
    )

    return filter_grad
