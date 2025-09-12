import tensorflow as tf

# Create a tensor
tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0])

# Quantize the tensor
quantized_tensor = tf.quantize_per_tensor(tensor, bitwidth=8)

# Print the quantized tensor
print("Quantized Tensor:")
print(quantized_tensor)

# Dequantize the tensor
dequantized_tensor = tf.dequantize(quantized_tensor)

# Print the dequantized tensor
print("Dequantized Tensor:")
print(dequantized_tensor)
