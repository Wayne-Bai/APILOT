
import tensorflow as tf

input_data = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=tf.dtypes.int8)
filter_data = tf.constant([[1, 0], [0, 1]], dtype=tf.dtypes.int8)
strides = [1, 1, 1, 1]
dilations = [1, 1, 1, 1]
padding = "VALID"

output = tf.raw_ops.QuantizedConv2D(input=input_data, filter=filter_data, strides=strides, dilations=dilations, padding=padding)

print(output)
