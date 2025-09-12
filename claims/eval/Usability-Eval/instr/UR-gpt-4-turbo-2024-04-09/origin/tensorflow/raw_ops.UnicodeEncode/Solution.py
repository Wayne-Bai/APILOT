import tensorflow as tf

def encode_ints_to_unicode(input_tensor):
    # TensorFlow's way to encode ints into Unicode strings using the `AsString` operation.
    return tf.strings.as_string(input_tensor)

# Example usage
input_tensor = tf.constant([65, 66, 67], dtype=tf.int32)
encoded_strings = encode_ints_to_unicode(input_tensor)
print(encoded_strings)
