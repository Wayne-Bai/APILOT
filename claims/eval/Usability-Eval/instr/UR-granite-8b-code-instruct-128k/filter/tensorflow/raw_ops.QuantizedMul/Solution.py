import tensorflow as tf

def raw_ops_element_wise_mul(x, y):
    return tf.raw_ops.QuantizedMul(x=x, y=y, Toutput=tf.float32)
