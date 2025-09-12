import tensorflow as tf

# Define the input tensor
x = tf.constant([0.5, 1.2, -0.3, 0.8])

# Define the min_range and max_range for quantization
min_range = tf.constant(0.0)
max_range = tf.constant(1.0)

# Perform the QuantizeAndDequantizeV4 operation
quantized = tf.raw_ops.QuantizeAndDequantizeV4(input=x, min_range=min_range, max_range=max_range)

# Print the quantized tensor
print(quantized)