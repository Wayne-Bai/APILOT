
import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0], dtype=tf.float32)

# Quantize the input tensor
quantized_tensor = tf.quantization.quantize_and_dequantize(input_tensor, 0.5, 128, tf.float32, tf.uint8)

# Print the quantized tensor
print(quantized_tensor)
