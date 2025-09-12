import tensorflow as tf

def quantized_conv2d(input_tensor, filter_tensor, min_input, max_input, min_filter, max_filter, strides, padding):
    # Quantize the input and filter tensors
    input_quantized = tf.quantization.fake_quant_with_min_max_args(input_tensor, min_input, max_input)
    filter_quantized = tf.quantization.fake_quant_with_min_max_args(filter_tensor, min_filter, max_filter)

    # Perform the convolution
    conv_output = tf.nn.conv2d(input_quantized, filter_quantized, strides=strides, padding=padding)

    return conv_output

# Example usage
input_tensor = tf.random.uniform([1, 28, 28, 3], dtype=tf.float32)
filter_tensor = tf.random.uniform([5, 5, 3, 16], dtype=tf.float32)
min_input, max_input = -1.0, 1.0
min_filter, max_filter = -1.0, 1.0
strides = [1, 1, 1, 1]
padding = 'SAME'

output = quantized_conv2d(input_tensor, filter_tensor, min_input, max_input, min_filter, max_filter, strides, padding)
print(output)
