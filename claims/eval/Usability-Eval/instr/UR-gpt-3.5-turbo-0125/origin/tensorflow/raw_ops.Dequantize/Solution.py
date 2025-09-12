
import tensorflow as tf

def dequantize_tensor(input_tensor, scale, min_range, max_range, signed=None):
    if signed is None:
        output_tensor = tf.cast(input_tensor, tf.float32) * scale
    else:
        output_tensor = tf.cast(input_tensor, tf.bfloat16) * scale

    return output_tensor

# Example usage
input_tensor = tf.constant([1, 2, 3, 4], dtype=tf.int8)
scale = 0.1
min_range = 0
max_range = 255
output_tensor = dequantize_tensor(input_tensor, scale, min_range, max_range)

print(output_tensor)
