import tensorflow as tf

def quantize_and_dequantize(tensor, num_bits=8):
    # Quantize the tensor
    min_val = tf.reduce_min(tensor)
    max_val = tf.reduce_max(tensor)
    scale = (max_val - min_val) / (2 ** num_bits - 1)
    quantized_tensor = tf.round((tensor - min_val) / scale)
    
    # Dequantize the tensor
    dequantized_tensor = quantized_tensor * scale + min_val
    
    return dequantized_tensor

# Example usage
tensor = tf.constant([0.1, 0.5, 0.9, 1.2], dtype=tf.float32)
dequantized_tensor = quantize_and_dequantize(tensor)

print(dequantized_tensor.numpy())
