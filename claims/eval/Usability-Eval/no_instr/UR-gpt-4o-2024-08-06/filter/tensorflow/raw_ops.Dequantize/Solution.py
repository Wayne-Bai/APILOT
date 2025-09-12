import tensorflow as tf

# Create a quantized input tensor
quantized_input = tf.constant([0, 64, 128, 255], dtype=tf.uint8)

# Specify the range for dequantization
min_range = tf.constant(0.0, dtype=tf.float32)
max_range = tf.constant(1.0, dtype=tf.float32)

# Perform dequantization
dequantized_output = tf.quantization.dequantize(
    quantized_input,
    min_range,
    max_range,
    mode='MIN_COMBINED'  # Mode can also be 'MIN_FIRST'
)

# Display the dequantized output
tf.print(dequantized_output)
