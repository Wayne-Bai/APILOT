
import tensorflow as tf

@tf.function(input_signature=[tf.TensorSpec(shape=[None], dtype=tf.float32), tf.TensorSpec(shape=[None], dtype=tf.float32)])
def add(a, b):
    return a + b
