import tensorflow as tf

# Create a placeholder tensor
input_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=tf.float32)

# Define the quantization parameters
min_range = tf.reduce_min(input_tensor)
max_range = tf.reduce_max(input_tensor)
num_bits = 8  # Number bits for the quantized data

# Quantize the tensor
quantized = tf.quantization.quantize(input_tensor, min_range, max_range, tf.qint8)

# Dequantize the tensor back to float32
dequantized = tf.quantization.dequantize(quantized.output, min_range, max_range)

# Run the operations in a session and print the result
print("Input Tensor:\n", input_tensor.numpy())
print("Dequantized Tensor:\n", dequantized.numpy())
