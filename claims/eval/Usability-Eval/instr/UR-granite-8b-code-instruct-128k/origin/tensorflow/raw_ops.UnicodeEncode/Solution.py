
import tensorflow as tf

def encode_tensor_into_unicode_strings(tensor):
    tensor_strings = tf.strings.as_string(tensor)
    return tensor_strings
