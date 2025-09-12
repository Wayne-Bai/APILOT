import tensorflow as tf

# Define quantized input and filter tensors
input_tensor = tf.constant([[[
    [1.0], [2.0], [3.0], [4.0]
], [
    [5.0], [6.0], [7.0], [8.0]
], [
    [9.0], [10.0], [11.0], [12.0]
], [
    [13.0], [14.0], [15.0], [16.0]
]]], dtype=tf.float32)

filter_tensor = tf.constant([[
    [[0.1]], [[0.2]]
], [
    [[0.3]], [[0.4]]
]], dtype=tf.float32)

# Quantize the input and filter tensors
quantized_input = tf.quantization.quantize(input_tensor, min_range=0.0, max_range=255.0, T=tf.qint32)
quantized_filter = tf.quantization.quantize(filter_tensor, min_range=0.0, max_range=255.0, T=tf.qint32)

# De-quantize the tensors for operations
dequantized_input = tf.quantization.dequantize(quantized_input.output, quantized_input.min_range, quantized_input.max_range)
dequantized_filter = tf.quantization.dequantize(quantized_filter.output, quantized_filter.min_range, quantized_filter.max_range)

# Prepare the convolution parameters
strides = [1, 1, 1, 1]
padding = 'VALID'

# Perform 2D convolution using the quantized tensors
conv_result = tf.nn.conv2d(dequantized_input, dequantized_filter, strides=strides, padding=padding)

# Print the output
print("Convolution result:")
print(conv_result.numpy())
