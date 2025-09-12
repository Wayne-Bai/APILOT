import tensorflow as tf

# Define the input tensor
input_tensor = tf.quantization.fake_quant_with_min_max_vars(
    tf.random.normal([1, 10, 10, 1]),
    min=-1.0,
    max=1.0,
    num_bits=8,
    narrow_range=False)

# Define the filter tensor
filter_tensor = tf.quantization.fake_quant_with_min_max_vars(
    tf.random.normal([3, 3, 1, 1]),
    min=-1.0,
    max=1.0,
    num_bits=8,
    narrow_range=False)

# Perform the 2D convolution
output_tensor = tf.raw_ops.QuantizedConv2D(
    input_tensor,
    filter_tensor,
    padding='SAME',
    dilations=[1, 1, 1, 1],
    strides=[1, 1, 1, 1],
    data_format='NHWC',
    dilations=[1, 1, 1, 1],
    padding='SAME',
    Tinput=tf.quint8,
    Tfilter=tf.quint8,
    Toutput=tf.quint8)

# Dequantize the output tensor
output_tensor = tf.quantization.fake_quant_with_min_max_vars(
    output_tensor,
    min=-1.0,
    max=1.0,
    num_bits=8,
    narrow_range=False)
