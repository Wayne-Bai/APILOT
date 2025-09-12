import tensorflow as tf

def create_ones_tensor(input_tensor):
    ones_tensor = tf.ones_like(input_tensor)
    return ones_tensor
