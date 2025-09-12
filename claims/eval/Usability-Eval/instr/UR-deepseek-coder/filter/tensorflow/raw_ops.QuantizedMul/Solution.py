import tensorflow as tf

def quantized_mul(x, y, min_x, max_x, min_y, max_y, Toutput=tf.dtypes.qint32):
    # Convert quantized inputs to float for multiplication
    x_float = tf.quantization.dequantize(x, min_x, max_x)
    y_float = tf.quantization.dequantize(y, min_y, max_y)
    
    # Perform element-wise multiplication in float
    result_float = x_float * y_float
    
    # Determine the range for the output
    min_result = tf.reduce_min(result_float)
    max_result = tf.reduce_max(result_float)
    
    # Quantize the result back to the desired output type
    result_quantized = tf.quantization.quantize(result_float, min_result, max_result, Toutput)
    
    return result_quantized

# Example usage:
# x_quantized = ...  # Quantized input tensor
# y_quantized = ...  # Quantized input tensor
# min_x = ...        # Minimum value of x
# max_x = ...        # Maximum value of x
# min_y = ...        # Minimum value of y
# max_y = ...        # Maximum value of y

# result = quantized_mul(x_quantized, y_quantized, min_x, max_x, min_y, max_y)
