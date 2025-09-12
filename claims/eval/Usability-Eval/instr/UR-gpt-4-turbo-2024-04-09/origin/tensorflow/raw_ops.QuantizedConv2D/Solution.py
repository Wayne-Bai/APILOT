import tensorflow as tf

# Define the quantized input and filter
# Typically, quantized tensors are represented as integers.
input_data = tf.random.normal([1, 10, 10, 3], dtype=tf.float32)
filter_data = tf.random.normal([3, 3, 3, 8], dtype=tf.float32)

# Quantize the input and filter to simulate quantized operation
input_min, input_max = tf.reduce_min(input_data), tf.reduce_max(input_data)
filter_min, filter_max = tf.reduce_min(filter_data), tf.reduce_max(filter_data)

# Convert floats to quantized values
q_input = tf.quantization.quantize(input_data, input_min, input_max, tf.quint8)
q_filter = tf.quantization.quantize(filter_data, filter_min, filter_max, tf.quint8)

# Use `tf.nn.quantized_conv2d` to perform the quantized convolution, which simulates the raw op behavior
# Note: this expects min/max to be scalars for the input and filter.
# Strides of 1 and 'SAME' padding
strides = [1, 1, 1, 1]
padding = 'SAME'

q_conv = tf.nn.quantized_conv2d(
    q_input.output, 
    q_filter.output, 
    q_input.min, 
    q_input.max, 
    q_filter.min, 
    q_filter.max, 
    strides, 
    padding)
