import tensorflow as tf

def conv2d(input_tensor, filter_tensor):
    return tf.raw_ops.Conv2D(input=input_tensor, filter=filter_tensor, strides=[1, 1, 1, 1], padding="VALID")
