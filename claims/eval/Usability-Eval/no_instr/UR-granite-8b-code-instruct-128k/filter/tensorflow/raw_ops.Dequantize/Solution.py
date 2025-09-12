import tensorflow as tf
# Create a quantized tensor
quantized_tensor = tf.constant([10, 20, 30], dtype=tf.quint8)
# Dequantize the tensor
dequantized_tensor = tf.raw_ops.Dequantize(input=quantized_tensor, dtype=tf.float32)
# Print the results
print(quantized_tensor)
print(dequantized_tensor)
