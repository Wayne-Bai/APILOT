import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([1.5, 2.3, 3.7, 4.2], dtype=tf.float32)

# Define the quantization parameters
min_range = tf.constant(0.0, dtype=tf.float32)
max_range = tf.constant(10.0, dtype=tf.float32)

# Quantize the input tensor
quantized_tensor = tf.quantization.quantize(input_tensor, min_range, max_range, tf.uint8)

# Dequantize the quantized tensor
dequantized_tensor = tf.quantization.dequantize(quantized_tensor, min_range, max_range)

# Calculate the gradient of the dequantized tensor with respect to the input tensor
grad, _ = tf.raw_ops.QuantizeAndDequantizeV4Grad(
    gradients=tf.constant([1.0, 1.0, 1.0, 1.0], dtype=tf.float32),
    inputs=input_tensor,
    min_range=min_range,
    max_range=max_range)

# Print the gradient
print(grad)
