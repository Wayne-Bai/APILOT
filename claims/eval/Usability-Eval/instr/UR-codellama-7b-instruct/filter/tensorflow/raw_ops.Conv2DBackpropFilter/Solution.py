
import tensorflow as tf

def conv2d(x, W):
    return tf.raw_ops.Conv2D(input=x, filter=W, padding="SAME")
