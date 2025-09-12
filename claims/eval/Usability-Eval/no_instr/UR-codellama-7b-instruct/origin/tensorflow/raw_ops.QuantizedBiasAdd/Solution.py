
import tensorflow as tf

# Define the quantized input tensor and the bias term
input = tf.constant([[1, 2], [3, 4]], dtype=tf.quint8)
bias = tf.constant([[5, 6], [7, 8]], dtype=tf.qint32)

# Add the bias term to the input tensor using raw_ops
output = tf.raw_ops.Add(input=input, bias=bias, data_format="NHWC")

print(output)
