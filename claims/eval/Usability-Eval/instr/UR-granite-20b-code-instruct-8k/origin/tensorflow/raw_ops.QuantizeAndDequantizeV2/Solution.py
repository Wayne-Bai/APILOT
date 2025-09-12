import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Quantize the input tensor
quantized_tensor = tf.quantization.quantize_and_dequantize(input_tensor)

# Dequantize the quantized tensor
dequantized_tensor = tf.quantization.quantize_and_dequantize(quantized_tensor, input_min=0.0, input_max=6.0)

# Print the dequantized tensor
print(dequantized_tensor.numpy())
