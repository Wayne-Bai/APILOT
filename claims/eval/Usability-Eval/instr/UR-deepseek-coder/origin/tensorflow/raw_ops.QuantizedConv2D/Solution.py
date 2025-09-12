import tensorflow as tf

def quantized_conv2d(input_tensor, filter_tensor, min_input, max_input, min_filter, max_filter, strides, padding):
    # Quantize the input and filter tensors
    input_quantized = tf.quantization.quantize(input_tensor, min_input, max_input, tf.qint8)
    filter_quantized = tf.quantization.quantize(filter_tensor, min_filter, max_filter, tf.qint8)
    
    # Dequantize the input and filter tensors
    input_dequantized = tf.quantization.dequantize(input_quantized[0], input_quantized[1], input_quantized[2])
    filter_dequantized = tf.quantization.dequantize(filter_quantized[0], filter_quantized[1], filter_quantized[2])
    
    # Perform the convolution
    conv_result = tf.nn.conv2d(input_dequantized, filter_dequantized, strides=strides, padding=padding)
    
    return conv_result

# Example usage:
# input_tensor = ... (your input tensor)
# filter_tensor = ... (your filter tensor)
# min_input = ... (minimum value of input tensor)
# max_input = ... (maximum value of input tensor)
# min_filter = ... (minimum value of filter tensor)
# max_filter = ... (maximum value of filter tensor)
# strides = [1, 1, 1, 1]  # Example strides
# padding = 'SAME'  # Example padding

# result = quantized_conv2d(input_tensor, filter_tensor, min_input, max_input, min_filter, max_filter, strides, padding)
