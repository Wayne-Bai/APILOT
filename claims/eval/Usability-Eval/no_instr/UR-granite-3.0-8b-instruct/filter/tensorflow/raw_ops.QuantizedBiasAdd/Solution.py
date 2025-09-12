import tensorflow as tf

def add_bias_quantized(input, bias):
    input_type = input.dtype
    bias_type = bias.dtype
    if input_type == tf.quint8 or input_type == tf.qint8 or input_type == tf.qint32:
        input = tf.raw_ops.QuantizeV2(input, tf.cast(tf.range(0, 256, dtype=input_type), input_type), tf.cast(tf.range(0, 256, dtype=input_type), input_type))
        bias = tf.raw_ops.QuantizeV2(bias, tf.cast(tf.range(0, 256, dtype=bias_type), bias_type), tf.cast(tf.range(0, 256, dtype=bias_type), bias_type))
    return tf.add(input, bias)
