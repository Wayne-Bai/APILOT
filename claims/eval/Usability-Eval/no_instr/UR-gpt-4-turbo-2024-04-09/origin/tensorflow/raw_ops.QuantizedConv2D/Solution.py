import tensorflow as tf

def quantized_conv2d(inputs, filters, strides, padding):
    """
    Perform a 2D convolution with quantized tensors.
    
    Args:
    inputs (tf.Tensor): A 4D input tensor with quantization parameters (min_input, max_input).
    filters (tf.Tensor): A 4D tensor of filters with quantization parameters (min_filter, max_filter).
    strides (list or tuple): The stride of the sliding window for each dimension of `inputs`.
    padding (str): Either 'SAME' or 'VALID' to specify the type of padding algorithm to use.

    Returns:
    tf.Tensor: A quantized 4D tensor resulting from the convolution operation.
    """
    # Min and max values for the inputs and filters
    min_input, max_input = tf.reduce_min(inputs), tf.reduce_max(inputs)
    min_filter, max_filter = tf.reduce_min(filters), tf.reduce_max(filters)

    # Quantization of inputs and filters
    input_quantized = tf.quantize_v2(inputs, min_input, max_input, tf.qint8, mode='SCALED')
    filter_quantized = tf.quantize_v2(filters, min_filter, max_filter, tf.qint8, mode='SCALED')

    # Convolution
    out = tf.nn.quantized_conv2d(input_quantized[0], filter_quantized[0], strides, padding,
                                 input_quantized[1], input_quantized[2], filter_quantized[1], filter_quantized[2])

    # Dequantize the output to float
    dequantized_output = tf.dequantize(out[0], out[1], out[2], dtype=tf.float32)

    return dequantized_output

# Example usage
# Define example tensors
input_tensor = tf.random.normal([1, 10, 10, 3])
filter_tensor = tf.random.normal([3, 3, 3, 8])
strides = [1, 1, 1, 1]
padding = 'SAME'

# Call the quantized convolution function
result = quantized_conv2d(input_tensor, filter_tensor, strides, padding)
print(result)
