
import tensorflow as tf

def quantized_conv2d(input_tensor, filter_tensor, strides, padding):
    return tf.raw_ops.QuantizedConv2D(input=input_tensor, filter=filter_tensor, strides=strides, padding=padding)

# Example Usage
input_tensor = tf.random.normal([1, 28, 28, 3])
filter_tensor = tf.random.normal([3, 3, 3, 64])
strides = [1, 1, 1, 1]
padding = "SAME"
output = quantized_conv2d(input_tensor, filter_tensor, strides, padding)

print(output)
