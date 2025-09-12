
import tensorflow as tf

def quantized_mul(x, y):
    return tf.raw_ops.QuantizedMul(x=x, y=y)
