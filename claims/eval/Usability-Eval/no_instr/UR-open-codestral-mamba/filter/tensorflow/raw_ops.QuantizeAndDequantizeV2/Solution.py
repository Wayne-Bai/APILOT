import tensorflow as tf

def quantize_and_dequantize(input_tensor, num_bits=8):
    input_min = tf.reduce_min(input_tensor)
    input_max = tf.reduce_max(input_tensor)

    input_range = tf.abs(input_max - input_min)
    quantize_range = 2**num_bits - 1
    key = 1

    # Quantization
    quantized_val = tf.clip_by_value(tf.math.divide((input_tensor - input_min), input_range) * quantize_range, 0.0, quantize_range)
    quantized_tensor = tf.quantize_and_dequantize_v2(quantized_val, 0.0, quantize_range, key, quantize_range)

    # Dequantization
    dequantized_tensor = tf.math.divide(quantized_tensor, (quantize_range / input_range)) + input_min

    return dequantized_tensor

# Testing
input_tensor = tf.constant([-10.0, -5.0, 0.0, 5.0, 10.0], dtype=tf.float32)
output_tensor = quantize_and_dequantize(input_tensor)
print(output_tensor)
