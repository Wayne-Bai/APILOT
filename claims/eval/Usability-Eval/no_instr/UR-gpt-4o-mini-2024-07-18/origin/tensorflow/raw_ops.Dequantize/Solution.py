import tensorflow as tf

# Example input tensor (quantized, e.g., int8 or int32) and scale/offset for dequantization
input_tensor = tf.constant([0, 127, 255], dtype=tf.int32)  # Example quantized values
scale = tf.constant(0.01, dtype=tf.float32)  # Scale
offset = tf.constant(0, dtype=tf.int32)  # Offset

# Dequantize the input tensor
dequantized_tensor = tf.experimental.numpy.multiply(tf.cast(input_tensor, tf.float32), scale)

# Print the dequantized tensor
print(dequantized_tensor)
