import tensorflow as tf

def dequantize_tensor(input_tensor, min_range, max_range, dtype=tf.float32, mode='MIN_COMBINED', narrow_range=False, axis=-1):
    # Using the current recommended function for dequantizing
    dequantized_tensor = tf.quantization.dequantize(
        input_tensor=input_tensor,
        min_range=min_range,
        max_range=max_range,
        dtype=dtype,
        mode=mode,
        narrow_range=narrow_range,
        axis=axis
    )
    return dequantized_tensor

# Example usage:
# Define a quantized tensor, with simulated min and max range typically found after quantization
quantized_tensor = tf.constant([0, 127, 255, 128, 100], dtype=tf.quint8)
min_val = 0.0
max_val = 1.0

# Perform dequantization
result_tensor = dequantize_tensor(quantized_tensor, min_val, max_val)
print("Dequantized Tensor:", result_tensor)
