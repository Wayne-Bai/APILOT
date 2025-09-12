# Import necessary TensorFlow module
import tensorflow as tf

# Define the input tensor with a quantized type (uint8) and shape [3]
input_tensor = tf.cast(tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype='int8'), tf.uint8)

# Define the bias tensor with a shape of [3]
bias = tf.constant([10, 20, 30], dtype='int32')

# Quantize the bias tensor to match the input tensor's type
quantized_bias = tf.quantization.fake_quant_with_min_max_args(bias, min=-128, max=127, num_bits=8)

# Add the quantized bias to the input tensor
output = tf.raw_ops.BiasAdd(input=input_tensor, bias=quantized_bias)

# Print the output
print(output)
