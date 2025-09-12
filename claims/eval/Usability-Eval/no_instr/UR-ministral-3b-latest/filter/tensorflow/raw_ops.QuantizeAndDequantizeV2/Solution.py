import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=tf.float32)

# Quantize the tensor
quantized_tensor = tf.raw_ops.MathQuantize(input_tensor, num_bits=8)

# Dequantize the tensor
dequantized_tensor = tf.raw_ops.MathDequantize(quantized_tensor)

# Print the results
print("Input Tensor:\n", input_tensor)
print("Quantized Tensor:\n", quantized_tensor)
print("Dequantized Tensor:\n", dequantized_tensor)
