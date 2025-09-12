import tensorflow as tf

def conv_input_grad(input_sizes, filter, out_backprop, strides, use_cudnn_on_gpu=True, padding="SAME"):
    """
    Computes the gradients of convolution with respect to the input.

    Args:
        input_sizes (Tensor): A 1-D tensor containing the size of the input.
        filter (Tensor): A 4-D tensor.
        out_backprop (Tensor): A 4-D tensor.
        strides (list): A list of integers representing the strides.
        use_cudnn_on_gpu (bool): Whether to use cuDNN for GPU computation.
        padding (str): A string specifying the padding.

    Returns:
        A tensor representing the gradients of convolution with respect to the input.
    """
    return tf.raw_ops.Conv2DBackpropInput(input_sizes, filter, out_backprop, strides, use_cudnn_on_gpu, padding)

# Example usage
if __name__ == "__main__":
    # Define the input sizes
    input_sizes = [1, 10, 10, 1]

    # Define the filter
    filter = tf.constant([[1, 2], [3, 4]])

    # Reshape the filter to a 4-D tensor
    filter = tf.reshape(filter, [2, 2, 1, 1])

    # Define the output backprop
    out_backprop = tf.constant([[[[1, 2], [3, 4]]]])

    # Define the strides
    strides = [1, 1, 1, 1]

    # Compute the gradients
    gradients = conv_input_grad(input_sizes, filter, out_backprop, strides)

    # Print the gradients
    print(gradients)
