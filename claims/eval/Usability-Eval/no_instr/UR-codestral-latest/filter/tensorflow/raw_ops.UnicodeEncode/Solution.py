import tensorflow as tf

def encode_tensor_to_unicode(tensor):
    return tf.strings.as_string(tensor)

# Example usage:
tensor = tf.constant([1, 2, 3, 4, 5])
encoded_tensor = encode_tensor_to_unicode(tensor)

print(encoded_tensor)
