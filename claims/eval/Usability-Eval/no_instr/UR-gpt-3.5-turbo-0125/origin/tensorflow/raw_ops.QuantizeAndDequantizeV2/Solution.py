
import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([1.5, 2.3, 3.7, 4.8])

# Quantize the input tensor
quantized_tensor = tf.quantization.quantize(input_tensor, min_range=0.0, max_range=10.0, num_bits=8, mode='MIN_COMBINED')

# Dequantize the quantized tensor
dequantized_tensor = tf.quantization.dequantize(quantized_tensor, min_range=0.0, max_range=10.0, num_bits=8, mode='MIN_COMBINED')

# Print the dequantized tensor
print(dequantized_tensor)
