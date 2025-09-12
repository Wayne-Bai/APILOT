import tensorflow as tf

# Create a tensor
tensor = tf.constant([1.2, 3.5, 4.7, 5.9])

# Quantize the tensor
quantized_tensor = tf.quantization.fake_quant_with_min_max_vars(tensor, tf.reduce_min(tensor), tf.reduce_max(tensor))

# Dequantize the tensor
dequantized_tensor = tf.quantization.dequantize(quantized_tensor, tf.reduce_min(tensor), tf.reduce_max(tensor))

# Print the original, quantized, and dequantized tensors
print("Original Tensor: ", tensor)
print("Quantized Tensor: ", quantized_tensor)
print("Dequantized Tensor: ", dequantized_tensor)
