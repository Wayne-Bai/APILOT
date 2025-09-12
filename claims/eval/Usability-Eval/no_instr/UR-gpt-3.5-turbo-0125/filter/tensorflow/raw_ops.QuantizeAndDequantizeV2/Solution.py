
import tensorflow as tf

def quantize_and_dequantize(input_tensor, min_range, max_range, out_type=tf.float32):
    # Quantize
    scale = (max_range - min_range) / 255.0
    zero_point = 128
    quantized_tensor = tf.cast(tf.round(input_tensor / scale + zero_point), tf.uint8)
    
    # Dequantize
    dequantized_tensor = tf.cast(quantized_tensor, out_type) * scale - zero_point * scale
    
    return dequantized_tensor

# Example Usage
input_tensor = tf.constant([1.5, 2.7, 3.3, 4.8])
min_range = 0
max_range = 10
result = quantize_and_dequantize(input_tensor, min_range, max_range)

print(result)
