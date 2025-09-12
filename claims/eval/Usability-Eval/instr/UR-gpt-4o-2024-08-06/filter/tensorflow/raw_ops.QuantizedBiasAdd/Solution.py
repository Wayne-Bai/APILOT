import tensorflow as tf

# Define the input tensor and bias tensor with quantized types
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.qint8)
bias_tensor = tf.constant([1, 2, 3], dtype=tf.qint8)

# Quantization parameters for the input and bias
input_min = tf.constant(-128.0, dtype=tf.float32)
input_max = tf.constant(127.0, dtype=tf.float32)
bias_min = tf.constant(-128.0, dtype=tf.float32)
bias_max = tf.constant(127.0, dtype=tf.float32)

# Use tf.nn.bias_add to add bias to the input on quantized types
output_tensor = tf.nn.bias_add(
    input_tensor, 
    bias_tensor, 
    name='quantized_bias_add'
)

# Convert the quantized output tensor to float for further processing or evaluation
output_float = tf.quantization.dequantize(
    output_tensor,
    min_range=input_min,
    max_range=input_max,  # Using input's range for simplicity, adjust if needed
    mode='MIN_FIRST'
)

# To visualize the result
print("Output Tensor in Float Format:")
print(output_float)
