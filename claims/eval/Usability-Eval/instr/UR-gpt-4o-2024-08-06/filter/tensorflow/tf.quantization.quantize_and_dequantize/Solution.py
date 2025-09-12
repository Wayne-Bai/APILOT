import tensorflow as tf

def quantize_and_dequantize(tensor, num_bits=8, range_min=None, range_max=None, round_mode='HALF_TO_EVEN', narrow_range=False):
    if range_min is None or range_max is None:
        range_min = tf.reduce_min(tensor)
        range_max = tf.reduce_max(tensor)
    
    # Quantization
    quantized_tensor = tf.quantization.fake_quant_with_min_max_vars(
        tensor,
        min=range_min,
        max=range_max,
        num_bits=num_bits,
        narrow_range=narrow_range
    )

    # Dequantization
    dequantized_tensor = quantized_tensor

    return dequantized_tensor

# Example usage
input_tensor = tf.constant([0.5, 0.8, 0.9, 1.0, 1.1], dtype=tf.float32)
quantized_dequantized_tensor = quantize_and_dequantize(input_tensor)

print("Original Tensor:", input_tensor.numpy())
print("Quantized then Dequantized Tensor:", quantized_dequantized_tensor.numpy())
