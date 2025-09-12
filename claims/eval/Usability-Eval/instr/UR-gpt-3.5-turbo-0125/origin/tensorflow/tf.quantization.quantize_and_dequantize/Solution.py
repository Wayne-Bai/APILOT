
import tensorflow as tf

def quantize_dequantize_tensor(input_tensor, num_bits=8):
    # Quantize the input tensor
    max_val = tf.reduce_max(input_tensor)
    min_val = tf.reduce_min(input_tensor)
    delta = (max_val - min_val) / (2**num_bits - 1)
    quantized_tensor = tf.round((input_tensor - min_val) / delta) * delta + min_val

    # Dequantize the quantized tensor
    dequantized_tensor = quantized_tensor

    return dequantized_tensor

# Example usage
input_tensor = tf.constant([-2, 0, 3, 5, 7], dtype=tf.float32)
dequantized_output = quantize_dequantize_tensor(input_tensor)
print(dequantized_output)
