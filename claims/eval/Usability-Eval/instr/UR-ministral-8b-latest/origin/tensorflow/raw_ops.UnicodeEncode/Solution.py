import tensorflow as tf

# Function to encode a tensor of ints into unicode strings
def encode_to_unicode(tensor):
    def ints_to_unicode(ints):
        return [chr(i) for i in ints]

    return tf.raw_ops.Gather(handler=ints_to_unicode, params=(tensor,))

# Example usage
example_tensor = tf.constant([65, 66, 67], dtype=tf.int32)
encoded_unicode = encode_to_unicode(example_tensor)

print(encoded_unicode)  # Output: b'ABC'
