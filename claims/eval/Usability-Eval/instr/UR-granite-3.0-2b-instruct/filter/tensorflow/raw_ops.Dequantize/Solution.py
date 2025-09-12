import tensorflow as tf

def dequantize_to_float(input_tensor):
    return tf.cast(input_tensor, tf.float32)

def dequantize_to_bfloat16(input_tensor):
    return tf.cast(input_tensor, tf.bfloat16)

# Example usage:
input_tensor = tf.random.normal([1, 3, 32, 32])  # Replace with your input tensor

dequantized_float_tensor = dequantize_to_float(input_tensor)
dequantized_bfloat16_tensor = dequantize_to_bfloat16(input_tensor)
