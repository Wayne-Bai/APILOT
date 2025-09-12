import tensorflow as tf

def quantized_conv2d(input_tensor, filter_tensor, strides, padding, dilations):
    # Ensure input and filter are of the same quantized type and shape
    assert input_tensor.dtype == tf.quint8, "input_tensor must be of type tf.quint8"
    assert filter_tensor.dtype == tf.quint8, "filter_tensor must be of type tf.quint8"

    # Specify minimum and maximum values for the input and filters
    min_input = tf.constant(0.0, dtype=tf.float32)
    max_input = tf.constant(255.0, dtype=tf.float32)
    min_filter = tf.constant(0.0, dtype=tf.float32)
    max_filter = tf.constant(255.0, dtype=tf.float32)

    # Define the quantized Conv2D operation
    output, min_output, max_output = tf.raw_ops.QuantizedConv2D(
        input=input_tensor,
        filter=filter_tensor,
        min_input=min_input,
        max_input=max_input,
        min_filter=min_filter,
        max_filter=max_filter,
        strides=strides,
        padding=padding,
        dilations=dilations
    )

    return output, min_output, max_output

# Example usage
# Define input and filter tensors (placeholders for actual values)
input_tensor = tf.constant([[[[1], [2]], [[3], [4]]]], dtype=tf.quint8)  # Shape: [1, 2, 2, 1]
filter_tensor = tf.constant([[[[1]], [[1]]], [[[1]], [[1]]]], dtype=tf.quint8)  # Shape: [2, 2, 1, 1]

# Specify strides and padding
strides = [1, 1, 1, 1]
padding = 'SAME'
dilations = [1, 1, 1, 1]

# Call the quantized_conv2d function
output, min_output, max_output = quantized_conv2d(input_tensor, filter_tensor, strides, padding, dilations)

# Print the output and its quantization range
print("Output:", output)
print("Min output:", min_output)
print("Max output:", max_output)
