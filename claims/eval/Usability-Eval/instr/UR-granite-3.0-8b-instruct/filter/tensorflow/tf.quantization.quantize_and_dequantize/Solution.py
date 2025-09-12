import tensorflow as tf

# Create a tensor
tensor = tf.constant([[1.2, 2.3], [3.4, 4.5]])

# Quantize the tensor
quantized_tensor = tf.quantization.fake_quant_with_min_max_vars(tensor, tf.reduce_min(tensor), tf.reduce_max(tensor))

# Dequantize the tensor
dequantized_tensor = tf.quantization.fake_dequantize(quantized_tensor)

# Print the original, quantized, and dequantized tensors
print("Original Tensor:\n", tensor.numpy())
print("Quantized Tensor:\n", quantized_tensor.numpy())
print("Dequantized Tensor:\n", dequantized_tensor.numpy())
