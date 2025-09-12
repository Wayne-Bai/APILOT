import tensorflow as tf

def dequantize(input, axis, dtype, name=None):
    return tf.raw_ops.Dequantize(input=input, axis=axis, dtype=dtype, name=name)
