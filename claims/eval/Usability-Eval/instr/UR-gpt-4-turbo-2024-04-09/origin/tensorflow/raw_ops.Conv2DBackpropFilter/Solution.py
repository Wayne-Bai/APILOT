import tensorflow as tf

def compute_gradient_wrt_filter(input, filter_shape, output_grad, strides, padding, dilations=None):
    """
    Computes the gradients of convolution with respect to the filter.

    Parameters:
    - input: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
    - filter_shape: A `Tensor`. Must have the same type as `input`. An integer tensor representing the shape of `filter`,
      where `filter` is a 4D `[filter_height, filter_width, in_channels, out_channels]` tensor.
    - output_grad: A `Tensor`. Must have the same type as `input`. 4-D with shape
      `[batch, height, width, channels]`.
    - strides: A list of `ints`. 1-D tensor of length 4. The stride of the sliding window for each dimension
      of `input`.
    - padding: A string from: `"SAME", "VALID"`. The type of padding algorithm to use.
    - dilations: An optional list of `ints`. Defaults to None. 1-D tensor of length 4. The dilation factor for each dimension
      of `input`.

    Returns:
    - A `Tensor`. Has the same type as `input`.
    """
    if dilations is None:
        dilations = [1, 1, 1, 1]

    # Use `tf.nn.conv2d_transpose` for computing the gradient of the filter
    grad_filter = tf.nn.grads.conv2d_backprop_input_v2(
        input_sizes=filter_shape,
        out_backprop=output_grad,
        filter=input,
        strides=strides,
        padding=padding,
        dilations=dilations
    )
    
    return grad_filter
