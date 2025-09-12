import tensorflow as tf

# Create a placeholder for the input quantized tensor
# Here, for example purposes, we specify int8 quantized input
input_tensor = tf.constant([0, 127, -128, 64], dtype=tf.qint8)

# Define the min and max range values for dequantization
min_range = tf.constant(-128.0, dtype=tf.float32)
max_range = tf.constant(127.0, dtype=tf.float32)

# Using tf.quantization.dequantize to dequantize the input tensor into float32
# or bfloat16 (here we use float32 for this example)
dequantized_tensor = tf.quantization.dequantize(
    input_tensor,
    min_range,
    max_range,
    mode='MIN_COMBINED'  # Choose the appropriate mode; MIN_COMBINED is quite common
)

# Print the dequantized tensor
print("Dequantized Tensor:", dequantized_tensor.numpy())
