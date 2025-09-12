import tensorflow as tf

def dequantize_tensor(input_tensor, scale, zero_point):
    # Dequantize the input tensor
    dequantized_tensor = tf.cast(input_tensor, tf.float32) * scale + zero_point
    return dequantized_tensor

# Example usage
input_tensor = tf.constant([0, 128, 255], dtype=tf.uint8)
scale = 0.01  # Example scale
zero_point = -1.0  # Example zero point

dequantized_result = dequantize_tensor(input_tensor, scale, zero_point)
print(dequantized_result.numpy())
