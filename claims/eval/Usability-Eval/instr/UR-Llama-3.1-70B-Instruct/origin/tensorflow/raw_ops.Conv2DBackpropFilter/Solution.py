# Import necessary libraries
import tensorflow as tf

# Define a function for computing gradients of convolution
def compute_conv_gradients(input, filters, out_backprop, strides, padding):
    """
    Computes the gradients of convolution with respect to the filter.

    Args:
        input (tf.Tensor): The input tensor.
        filters (tf.Tensor): The filter tensor.
        out_backprop (tf.Tensor): The output backprop tensor.
        strides (list): The strides for the convolution.
        padding (str): The padding for the convolution ('SAME' or 'VALID').

    Returns:
        tf.Tensor: The gradients of convolution with respect to the filter.
    """
    return tf.raw_ops.Conv2DBackpropFilter(
        input=input,
        filter_sizes=filters.shape,
        out_backprop=out_backprop,
        strides=strides,
        padding=padding.upper()
    )

# Example usage:
if __name__ == "__main__":
    # Define input and filter tensors
    input_tensor = tf.random.normal([1, 10, 10, 3])
    filter_tensor = tf.random.normal([3, 3, 3, 1])

    # Define output backprop tensor
    out_backprop = tf.random.normal([1, 10, 10, 1])

    # Define strides and padding
    strides = [1, 2, 2, 1]
    padding = 'SAME'

    # Compute gradients of convolution
    gradients = compute_conv_gradients(input_tensor, filter_tensor, out_backprop, strides, padding)

    print(gradients.shape)
