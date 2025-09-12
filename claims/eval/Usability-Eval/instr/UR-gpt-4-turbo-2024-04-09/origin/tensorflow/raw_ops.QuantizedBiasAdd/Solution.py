import tensorflow as tf

def quantized_bias_add(input, bias, min_input, max_input, min_bias, max_bias):
    # The function tf.quantization.quantized_add can be used to simulate quantized bias adding
    added, min_added, max_added = tf.quantization.quantize_v2(input, min_input, max_input, tf.qint32)
    bias_quantized, min_bias_quantized, max_bias_quantized = tf.quantization.quantize_v2(bias, min_bias, max_bias, tf.qint32)
    
    # Adding quantized values
    output, min_output, max_output = tf.quantization.quantized_add(added, bias_quantized, min_added, max_added, min_bias_quantized, max_bias_quantized)
    
    # The output is still quantized, convert it back to float for further use
    dequantized_output = tf.quantization.dequantize(output, min_output, max_output)
    
    return dequantized_output
    
# Example usage:
input_tensor = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
bias_tensor = tf.constant([0.5, 0.5, 0.5], dtype=tf.float32)
min_input, max_input = 0.0, 4.0
min_bias, max_bias = 0.0, 1.0

output_tensor = quantized_bias_add(input_tensor, bias_tensor, min_input, max_input, min_bias, max_bias)
print(output_tensor)
