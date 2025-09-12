
import tensorflow as tf

# Define the input and filter tensors
input_quantized = tf.quantized(input, min_input, max_input, Tinput=tf.quint8)
filter_quantized = tf.quantized(filter, min_filter, max_filter, Tfilter=tf.quint8)

# Compute the convolution
output, min_output, max_output = tf.raw_ops.QuantizedConv2D(
    input=input_quantized,
    filter=filter_quantized,
    min_input=min_input,
    max_input=max_input,
    min_filter=min_filter,
    max_filter=max_filter,
    Tinput=tf.quint8,
    Tfilter=tf.quint8,
    Toutput=tf.qint32,
    strides=[1, 1, 1, 1],
    padding='SAME'
)

# Dequantize the output tensor
output_dequantized = tf.dequantize(output, min_output, max_output)
