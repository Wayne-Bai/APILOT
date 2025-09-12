
import tensorflow as tf

def maxpooling_grad(input, grad, ksize, strides, padding, data_format):
    return tf.raw_ops.MaxPoolGrad(input=input, grad=grad, ksize=ksize, strides=strides, padding=padding, data_format=data_format)
