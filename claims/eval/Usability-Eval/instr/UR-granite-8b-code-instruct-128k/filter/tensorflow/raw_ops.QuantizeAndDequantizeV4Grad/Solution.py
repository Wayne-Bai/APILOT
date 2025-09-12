import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[0.5, 0.7], [-0.2, 0.3]])

# Quantize the input tensor
quantized_tensor = tf.quantize_v2(input_tensor, 0.0, 1.0, tf.uint8)

# Dequantize the quantized tensor
dequantized_tensor = tf.dequantize(quantized_tensor)

# Calculate the gradient of QuantizeAndDequantizeV4
grad_tensor = tf.raw_ops.QuantizeAndDequantizeV4Grad(input=input_tensor, gradient=dequantized_tensor)

# Print the gradient tensor
print(grad_tensor)
