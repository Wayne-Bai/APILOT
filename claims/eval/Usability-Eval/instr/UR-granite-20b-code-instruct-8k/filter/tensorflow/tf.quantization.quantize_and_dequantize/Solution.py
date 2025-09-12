import tensorflow as tf

# Define the tensor to be quantized and dequantized
input_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]])

# Quantize the tensor
quantized_tensor = tf.quantization.quantize_and_dequantize(input_tensor, 0.5, 128, True)

# Dequantize the tensor
dequantized_tensor = tf.quantization.quantize_and_dequantize(quantized_tensor, 0.5, 128, False)
