import tensorflow as tf

def quantize_and_dequantize(input_tensor, num_bits=8, range_given=False, input_min=0.0, input_max=0.0):
    # Quantize the input tensor
    min_range = tf.reduce_min(input_tensor)
    max_range = tf.reduce_max(input_tensor)
    
    if range_given:
        min_range = input_min
        max_range = input_max
    
    scale = (max_range - min_range) / (2 ** num_bits - 1)
    quantized_tensor = tf.round((input_tensor - min_range) / scale)
    
    # Dequantize the quantized tensor
    dequantized_tensor = quantized_tensor * scale + min_range
    
    return dequantized_tensor

# Example usage
input_tensor = tf.constant([0.1, 0.5, 0.9, 1.0], dtype=tf.float32)
dequantized_output = quantize_and_dequantize(input_tensor)

print(dequantized_output.numpy())
