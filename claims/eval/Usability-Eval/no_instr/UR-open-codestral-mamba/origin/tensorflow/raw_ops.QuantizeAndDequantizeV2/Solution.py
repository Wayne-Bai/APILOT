import tensorflow as tf

def quantize_dequantize(input_tensor):
    quantized_tensor = tf.fake_quant_with_min_max_vars(
        input_tensor,
        min=tf.constant(0, dtype=tf.float32),
        max=tf.constant(1, dtype=tf.float32),
        num_bits=8
    )

    dequantized_tensor = tf.fake_quant_dequantize(
        quantized_tensor,
        min=tf.constant(0, dtype=tf.float32),
        max=tf.constant(1, dtype=tf.float32)
    )

    return dequantized_tensor

# Example usage
input_tensor = tf.constant([0.1, 0.2, 0.3, 0.4, 0.5], dtype=tf.float32)
output_tensor = quantize_dequantize(input_tensor)
print(output_tensor)
