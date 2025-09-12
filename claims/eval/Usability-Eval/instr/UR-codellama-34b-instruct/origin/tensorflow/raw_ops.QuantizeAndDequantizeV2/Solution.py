import tensorflow as tf

# Load your data into a tensor
data = ...

# Quantize the tensor using the `tf.quantization.quantize` function
quantized_data = tf.quantization.quantize(data, num_bits=8)

# Dequantize the quantized tensor using the `tf.quantization.dequantize` function
dequantized_data = tf.quantization.dequantize(quantized_data, num_bits=8)
