import tensorflow as tf

# Function to quantize and dequantize a tensor
def quantize_and_dequantize_tensor(tensor, num_bits=8):
    # Determine the range based on the input tensor
    min_val = tf.reduce_min(tensor)
    max_val = tf.reduce_max(tensor)
    
    # Quantize the tensor
    scale = (max_val - min_val) / (2**num_bits - 1)
    zero_point = tf.round(-min_val / scale)
    
    # Clipping the zero_point to ensure it falls within the valid range
    zero_point = tf.clip_by_value(zero_point, 0, 2**num_bits - 1)
    
    # Quantization
    quantized_tensor = tf.round(tensor / scale + zero_point)
    
    # Dequantization
    dequantized_tensor = (quantized_tensor - zero_point) * scale
    
    return dequantized_tensor

# Example usage
input_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)
output_tensor = quantize_and_dequantize_tensor(input_tensor)

print("Input Tensor:\n", input_tensor.numpy())
print("Output Tensor:\n", output_tensor.numpy())
