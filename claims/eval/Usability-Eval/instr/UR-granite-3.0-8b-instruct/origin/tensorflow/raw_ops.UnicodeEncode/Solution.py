import tensorflow as tf

def int_to_unicode(input_tensor):
    # Ensure the input tensor is of type int32
    input_tensor = tf.cast(input_tensor, tf.int32)

    # Encode the tensor of ints into unicode strings
    unicode_strings = tf.strings.unicode_encode_utf8(input_tensor)

    return unicode_strings
