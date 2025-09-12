
import tensorflow as tf

# Define the tensor to be quantized and dequantized
tensor = tf.constant([1.5, 2.3, 3.7])

# Quantize the tensor
quantized_tensor = tf.quantization.quantize_and_dequantize(tensor)

# Dequantize the tensor
dequantized_tensor = quantized_tensor.dequantize()
