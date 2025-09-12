import tensorflow as tf

def quantized_conv2d(input_tensor, filter_tensor, strides=(1, 1), padding='VALID'):
    """
    Computes a 2D Convolution with quantized input and filters.

    Args:
    - input_tensor: Quantized input 4D tensor of shape (batch_size, height, width, channels).
    - filter_tensor: Quantized filter 4D tensor of shape (num_filters, kernel_height, kernel_width, in_channels).
    - strides: Stride of the convolution. Defaults to (1, 1).
    - padding: Type of padding to use. Supports 'VALID' or 'SAME'. Defaults to 'VALID'.

    Returns:
    - The quantized convolution output tensor.
    """
    # Convert quantized tensors to float to perform the operation
    quantized_input = tf.cast(input_tensor, dtype=tf.float32)
    quantized_filter = tf.cast(filter_tensor, dtype=tf.float32)

    # Perform the convolution operation
    raw_op = tf.raw_ops.Conv2D(
        input=quantized_input,
        filters=quantized_filter,
        strides=strides,
        padding=padding
    )

    # Convert the output back to the quantized data type
    quantized_output = tf.cast(raw_op, quantized_input.dtype)

    return quantized_output

# Example usage
input_tensor = tf.constant(  # Assuming appropriate shape and dtype for a quantized tensor
    [[[[1, 2], [3, 4]],
      [[5, 6], [7, 8]]]], dtype=tf.quantization.qubit)

filter_tensor = tf.constant(  # Assuming appropriate shape and dtype for a quantized tensor
    [[[[1, 1],
       [1, 1]]]], dtype=tf.quantization.qubit)

output_tensor = quantized_conv2d(input_tensor, filter_tensor)
