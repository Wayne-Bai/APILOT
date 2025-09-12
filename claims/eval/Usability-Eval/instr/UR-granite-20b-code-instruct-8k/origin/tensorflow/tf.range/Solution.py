import tensorflow as tf

def generate_sequence(start, end, step):
    return tf.range(start, end, step)
