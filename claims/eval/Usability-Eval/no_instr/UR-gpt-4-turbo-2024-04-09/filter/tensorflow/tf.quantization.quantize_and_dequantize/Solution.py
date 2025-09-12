import tensorflow as tf

def quantize_and_dequantize(tensor, num_bits, signed_input):
    # Quantizing the tensor
    quantized = tf.quantization.quantize(tensor, tf.reduce_min(tensor), tf.reduce_max(tensor), tf.quint8, mode='MIN_COMBINED')
    
    # Dequantizing the tensor
    dequantized = tf.quantization.dequantize(quantized.output, quantized.output_min, quantized.output_max, dtype=tf.float32)
    
    return dequantized

# Example usage
tensor = tf.constant([1.0, 2.0, 3.0, 4.0])
num_bits = 8
signed_input = False
result = quantize_and_dequantize(tensor, num_bits, signed_input)

print("Original tensor:", tensor.numpy())
print("After quantization and dequantization:", result.numpy())
