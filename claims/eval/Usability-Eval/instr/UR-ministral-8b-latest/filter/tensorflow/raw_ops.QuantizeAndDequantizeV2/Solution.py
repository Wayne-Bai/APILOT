import tensorflow as tf

# Function to quantize and dequantize a tensor
def quantize_dequantize_tensor(tensor):
    # Quantize the tensor
    quantized_tensor = tf.raw_ops.Quantize(tensor, 't1')._quantized_tensor

    # Dequantize the tensor
    dequantized_tensor = tf.raw_ops.Dequantize(quantized_tensor, 'u3')._dequantized_tensor

    return dequantized_tensor

# Example usage
tensor = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)
quantized_tensor = quantize_dequantize_tensor(tensor)
print(quantized_tensor)
