
import tensorflow as tf

def quantize_dequantize(input_tensor):
    quantized_tensor = tf.quantization.quantize(input_tensor, min_range=-1.0, max_range=1.0, mode='MIN_COMBINED', round_mode='HALF_AWAY_FROM_ZERO')
    dequantized_tensor = tf.cast(quantized_tensor[0], tf.float32) * quantized_tensor[1]
    return dequantized_tensor

# Example usage
input_tensor = tf.constant([-0.5, 0.2, 0.8, -0.3])
result = quantize_dequantize(input_tensor)
print(result)
