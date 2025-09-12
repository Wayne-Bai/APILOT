import tensorflow as tf

def quantize_and_dequantize(tensor, num_bits):
    min_val = tf.reduce_min(tensor)
    max_val = tf.reduce_max(tensor)

    # Quantize
    quantized = tf.quantization.quantize(
        tensor,
        min_val,
        max_val,
        tf.quint8,  # Using 8-bit unsigned integers
        mode='MIN_COMBINED',
        round_mode='HALF_TO_EVEN'
    ).output

    # Dequantize
    dequantized = tf.quantization.dequantize(
        quantized,
        min_val,
        max_val,
        mode='MIN_COMBINED'
    )

    return dequantized

# Example usage:
tensor = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)
result = quantize_and_dequantize(tensor, num_bits=8)
print("Original tensor:", tensor.numpy())
print("After quantization and dequantization:", result.numpy())
