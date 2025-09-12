import tensorflow as tf

def quantized_conv2d(input, filter, strides, padding):
    quantized_input = tf.quantization.quantize_and_dequantize(input, -1, 1)
    quantized_filter = tf.quantization.quantize_and_dequantize(filter, -1, 1)
    conv = tf.nn.conv2d(quantized_input, quantized_filter, strides, padding)
    return tf.quantization.quantize_and_dequantize(conv, -1, 1)
