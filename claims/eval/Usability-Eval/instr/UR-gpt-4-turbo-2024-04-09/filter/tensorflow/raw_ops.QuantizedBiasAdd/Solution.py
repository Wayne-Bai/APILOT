import tensorflow as tf

def quantized_bias_add(input_tensor, bias_tensor, input_min, input_max, bias_min, bias_max):
    input_tensor_quantized = tf.quantization.quantize(input_tensor, input_min, input_max, tf.quint8)
    bias_tensor_quantized = tf.quantization.quantize(bias_tensor, bias_min, bias_max, tf.quint32)
    
    added_tensor = tf.raw_ops.QuantizedBiasAdd(input=input_tensor_quantized.output,
                                               bias=bias_tensor_quantized.output,
                                               min_input=input_tensor_quantized.output_min,
                                               max_input=input_tensor_quantized.output_max,
                                               min_bias=bias_tensor_quantized.output_min,
                                               max_bias=bias_tensor_quantized.output_max)
    
    added_tensor_dequantized = tf.quantization.dequantize(added_tensor.output,
                                                          added_tensor.min_output,
                                                          added_tensor.max_output)
    return added_tensor_dequantized

# Example usage:
input_tensor = tf.constant([1.2, 3.4, 5.6], dtype=tf.float32)
bias_tensor = tf.constant([0.1, 0.2, 0.3], dtype=tf.float32)

# Assuming the ranges are known or calculated
input_min, input_max = 0.0, 6.0
bias_min, bias_max = 0.0, 0.5

result = quantized_bias_add(input_tensor, bias_tensor, input_min, input_max, bias_min, bias_max)
print(result)
