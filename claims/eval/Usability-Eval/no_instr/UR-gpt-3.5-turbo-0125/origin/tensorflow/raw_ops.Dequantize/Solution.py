
import tensorflow as tf

def dequantize_tensor(input_tensor):
    return tf.quantization.dequantize(input_tensor, tf.uint8, mode='MIN_COMBINED', round_mode='HALF_TO_EVEN')

# Usage example:
input_tensor = tf.constant([1, 2, 3, 4], dtype=tf.uint8)
output_tensor = dequantize_tensor(input_tensor)
print(output_tensor)
