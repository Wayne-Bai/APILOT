import tensorflow as tf

# Create a tensor to quantize and dequantize
tensor = tf.random.uniform((100, 100))

# Quantize the tensor
quantized_tensor = tf.quantization.quantize(tensor)

# Dequantize the tensor
dequantized_tensor = tf.quantization.dequantize(quantized_tensor)

# Print the original and dequantized tensors
print("Original tensor:")
print(tensor)
print("Dequantized tensor:")
print(dequantized_tensor)
