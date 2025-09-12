import tensorflow as tf

# Create a tensor
tensor = tf.constant([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]], dtype=tf.float32)

# Define the quantization range
input_min = tf.reduce_min(tensor)
input_max = tf.reduce_max(tensor)

# Quantize the tensor
scale = (input_max - input_min) / 255.0
quantized_tensor = tf.cast((tensor - input_min) / scale, tf.uint8)

# Dequantize the tensor
dequantized_tensor = (tf.cast(quantized_tensor, tf.float32) * scale) + input_min
