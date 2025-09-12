import tensorflow as tf

# Create a quantized tensor
quantized_tensor = tf.constant([10, 20, 30, 40], dtype=tf.quint8)

# Dequantize the tensor
dequantized_tensor = tf.raw_ops.Dequantize(input=quantized_tensor, min_range=0.0, max_range=50.0, mode="MIN_FIRST")

# Print the dequantized tensor
print(dequantized_tensor)
