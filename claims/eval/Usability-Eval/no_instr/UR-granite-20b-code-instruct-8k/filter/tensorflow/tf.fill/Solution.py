import tensorflow as tf

def create_scalar_tensor(value):
    return tf.fill([1], value)
