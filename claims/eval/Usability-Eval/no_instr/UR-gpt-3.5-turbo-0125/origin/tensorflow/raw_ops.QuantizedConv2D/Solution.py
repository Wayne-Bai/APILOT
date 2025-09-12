
import tensorflow as tf

def quantized_conv2d(input, filter, **kwargs):
    return tf.raw_ops.QuantizedConv2D(input=input, filter=filter, **kwargs)
