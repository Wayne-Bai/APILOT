import tensorflow as tf

def substrings_from_tensor(tensor):
    substrings = tf.strings.split(tensor, sep=' ')
    return substrings
