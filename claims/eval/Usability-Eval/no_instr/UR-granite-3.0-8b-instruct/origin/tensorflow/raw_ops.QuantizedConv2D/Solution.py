import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant(np.random.rand(1, 28, 28, 1), dtype=tf.float32)

# Define the filter tensor
filter_tensor = tf.constant(np.random.rand(3, 3, 1, 1), dtype=tf.float32)

# Quantize the input and filter tensors
input_tensor_quantized = tf.quantization.quantize_v2(input_tensor)
filter_tensor_quantized = tf.quantization.quantize_v2(filter_tensor)

# Compute the 2D convolution
output_tensor = tf.raw_ops.QuantizedConv2D(
    input=input_tensor_quantized,
    filter=filter_tensor_quantized,
    strides=[1, 1, 1, 1],
    padding="SAME",
    dilations=[1, 1, 1, 1]
)

# Dequantize the output tensor
output_tensor_dequantized = tf.quantization.dequantize(output_tensor)
