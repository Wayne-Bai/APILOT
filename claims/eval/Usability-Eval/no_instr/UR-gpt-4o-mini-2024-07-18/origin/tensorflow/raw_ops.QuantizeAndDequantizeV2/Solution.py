import tensorflow as tf

def quantize_dequantize_tensor(input_tensor, num_bits=8):
    # Quantize the input tensor
    min_val = tf.reduce_min(input_tensor)
    max_val = tf.reduce_max(input_tensor)

    # Scale the input tensor to the range of [0, 2^num_bits - 1]
    scale = (max_val - min_val) / (2**num_bits - 1)
    zero_point = -tf.round(min_val / scale)

    # Clip zero point to ensure it falls within the quantization range
    zero_point = tf.clip_by_value(zero_point, 0, 2**num_bits - 1)
    
    # Perform quantization
    quantized_tensor = tf.round((input_tensor - min_val) / scale + zero_point)
    quantized_tensor = tf.clip_by_value(quantized_tensor, 0, 2**num_bits - 1)

    # Dequantize the tensor
    dequantized_tensor = scale * (tf.cast(quantized_tensor, tf.float32) - zero_point) + min_val
    
    return quantized_tensor, dequantized_tensor

# Example usage
input_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
quantized, dequantized = quantize_dequantize_tensor(input_tensor)
print("Quantized Tensor:\n", quantized.numpy())
print("Dequantized Tensor:\n", dequantized.numpy())
