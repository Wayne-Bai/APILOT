
import tensorflow as tf

input_data = tf.constant(...)  # 4D tensor for input data
filter_data = tf.constant(...)  # 4D tensor for filter data
strides = [1, 1, 1, 1]
padding = 'SAME'

output = tf.raw_ops.QuantizedConv2D(input=input_data, filter=filter_data, strides=strides, padding=padding)

