import tensorflow as tf

def quantize_and_dequantize(tensor, num_bits=8, range_given=False, input_min=0.0, input_max=1.0):
    # Quantize the tensor
    scale, min_val = tf.nn.min_max_quantization_params(tensor, num_bits=num_bits, narrow_range=False)
    quantized_tensor = tf.quantization.quantize(tensor, min_val, min_val + scale * (2 ** num_bits - 1), tf.qint8)
    
    # Dequantize the tensor
    dequantized_tensor = tf.quantization.dequantize(quantized_tensor, min_val, min_val + scale * (2 ** num_bits - 1))
    
    return dequantized_tensor

# Example usage
tensor = tf.constant([0.1, 0.5, 0.9])
result = quantize_and_dequantize(tensor)
print(result)
