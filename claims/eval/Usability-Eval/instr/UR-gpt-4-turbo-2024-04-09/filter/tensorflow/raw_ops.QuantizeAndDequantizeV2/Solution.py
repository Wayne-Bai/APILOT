import tensorflow as tf

def quantize_dequantize(x, min_range, max_range, T, mode='MIN_COMBINED', round_mode='HALF_TO_EVEN'):
    # Quantize the tensor
    quantized = tf.quantization.quantize(x, min_range, max_range, T, mode=mode)
    # Extract the quantized tensor and the actual min and max ranges used
    quantized_tensor, actual_min, actual_max = quantized
    # Dequantize the tensor
    dequantized = tf.quantization.dequantize(quantized_tensor, actual_min, actual_max, dtype=tf.float32, mode=mode)
    return dequantized

# Example usage:
x = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)
min_range = 0.0
max_range = 4.0

result = quantize_dequantize(x, min_range, max_range, tf.quint8)
print(result)
