import tensorflow as tf

def compute_conv_gradients(
    input_: tf.Tensor, 
    filter_: tf.Tensor, 
    out_backprop: tf.Tensor, 
    strides: list, 
    padding: str, 
    data_format: str = "NDHWC"
):
    """
    Computes the gradients of convolution with respect to the input.

    Args:
    - input_: A Tensor. The input.
    - filter_: A Tensor. The filter.
    - out_backprop: A Tensor. The gradients of the output.
    - strides: A list of ints. The strides of the convolution.
    - padding: A string from "SAME", "VALID". The type of padding algorithm.
    - data_format: An optional string from: "NDHWC", "NCDHW". Defaults to "NDHWC".

    Returns:
    A Tensor. The gradients of convolution with respect to the input.
    """

    # Compute the gradients of convolution with respect to the input
    conv_gradients = tf.raw_ops.Conv2DBackpropInput(
        input_sizes=[input_.shape[0], input_.shape[1], input_.shape[2], input_.shape[3]],
        filter=filter_,
        out_backprop=out_backprop,
        strides=strides,
        padding=padding.upper(),
        data_format=data_format.upper()
    )

    return conv_gradients


# Example usage
if __name__ == "__main__":
    # Create some dummy data
    input_data = tf.random.uniform((1, 5, 5, 3))
    filter_data = tf.random.uniform((3, 3, 3, 2))
    out_backprop = tf.random.uniform((1, 5, 5, 2))

    # Define the strides and padding
    strides = [1, 1, 1, 1]
    padding = "SAME"

    # Compute the gradients of convolution with respect to the input
    gradients = compute_conv_gradients(
        input_data, filter_data, out_backprop, strides, padding
    )

    print(gradients)
