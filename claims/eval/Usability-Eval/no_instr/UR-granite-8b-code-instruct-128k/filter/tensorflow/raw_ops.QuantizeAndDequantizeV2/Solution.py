import tensorflow as tf

# Create a tensor to quantize and dequantize
x = tf.constant([0.2, 0.4, 0.6, 0.8])

# Quantize the tensor
x_quantized = tf.quantize_v2(x, min_range=0.0, max_range=1.0, dtype=tf.quint8)

# Dequantize the tensor
x_dequantized = tf.dequantize_v2(x_quantized, min_range=0.0, max_range=1.0, dtype=tf.float32)

# Print the results
print("Original Tensor:", x)
print("Quantized Tensor:", x_quantized)
print("Dequantized Tensor:", x_dequantized)
