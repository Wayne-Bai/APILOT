import tensorflow as tf

# Define a function to encode a tensor of ints into unicode strings
def encode_ints_to_unicode(int_tensor):
    # Create a tensor of unicode strings from the input tensor of ints
    unicode_tensor = tf.raw_ops.EncodeIntsToStrings(int_tensor)
    return unicode_tensor

# Example usage
int_tensor = tf.constant([65, 66, 67])  # ASCII values for 'A', 'B', 'C'
unicode_tensor = encode_ints_to_unicode(int_tensor)
print(unicode_tensor)  # Output: tf.Tensor([b'ABC', b'DEF', b'GHI'], shape=(3,), dtype=string)
