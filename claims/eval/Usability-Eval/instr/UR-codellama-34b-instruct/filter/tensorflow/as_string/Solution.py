import tensorflow as tf

def convert_to_string(x):
    return tf.strings.reduce_join(tf.constant([str(xi) for xi in x]))
