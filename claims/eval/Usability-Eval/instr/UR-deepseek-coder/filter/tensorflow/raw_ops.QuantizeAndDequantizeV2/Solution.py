import tensorflow as tf

def quantize_and_dequantize(input_tensor, input_min, input_max, num_bits=8, range_given=True, signed_input=True):
    # Quantize the input tensor
    scale = (input_max - input_min) / (2 ** num_bits - 1)
    quantized_tensor = tf.round((input_tensor - input_min) / scale)
    
    # Clip the quantized tensor to the valid range
    if signed_input:
        quantized_tensor = tf.clip_by_value(quantized_tensor, -2 ** (num_bits - 1), 2 ** (num_bits - 1) - 1)
    else:
        quantized_tensor = tf.clip_by_value(quantized_tensor, 0, 2 ** num_bits - 1)
    
    # Dequantize the quantized tensor
    dequantized_tensor = quantized_tensor * scale + input_min
    
    return dequantized_tensor

# Example usage
input_tensor = tf.constant([0.5, 1.5, 2.5], dtype=tf.float32)
input_min = 0.0
input_max = 3.0
num_bits = 8

dequantized_output = quantize_and_dequantize(input_tensor, input_min, input_max, num_bits)
print(dequantized_output.numpy())
