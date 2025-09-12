import tensorflow as tf

def tensor_to_string(tensor):
    tensor = tf.strings.as_string(tensor)
    return tensor
