import tensorflow as tf

def quantize_and_dequantize(tensor):
    # Quantize the tensor to 8-bits representation
    quantized_tensor = tf.quantization.quantize(tensor, tf.reduce_min(tensor), tf.reduce_max(tensor), tf.quint8)    
    # Dequantize the tensor back to floating point
    dequantized_tensor = tf.quantization.dequantize(quantized_tensor.output, quantized_tensor.min_range, quantized_tensor.max_range)
    return dequantized_tensor

# Example usage:
tensor = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)
result = quantize_and_dequantize(tensor)
print(result)
