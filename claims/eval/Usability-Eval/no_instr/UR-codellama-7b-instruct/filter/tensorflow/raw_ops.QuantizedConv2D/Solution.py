import tensorflow as tf

# Define the quantized 4D input and filter tensors
input_tensor = tf.constant([[[[0, 1], [2, 3]]]], dtype=tf.int8)
filter_tensor = tf.constant([[[[1, 2], [3, 4]]]], dtype=tf.int8)

# Perform the convolution operation
conv_output = tf.raw_ops.QuantizedConv2D(input=input_tensor, filter=filter_tensor, strides=[1, 1, 1, 1], padding='SAME')
print(conv_output)
