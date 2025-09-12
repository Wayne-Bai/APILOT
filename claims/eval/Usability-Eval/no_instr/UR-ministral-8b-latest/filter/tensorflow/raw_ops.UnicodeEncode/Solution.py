import tensorflow as tf

def ints_to_unicode(strings):
    def _encode(s):
        if isinstance(s, tf.RaggedTensor):
            return tf.raw_ops.RawRaggedStringsStringEncode(s)
        elif isinstance(s, tf.Tensor):
            return tf.raw_ops.RawStringsStringEncode(s)
        elif isinstance(s, (str, bytes)):
            return tf.constant([s])
        else:
            raise TypeError(f"Unsupported input type: {type(s)}")

    return tf.map_fn(lambda x: _encode(x), strings)

# Example usage:
strings = tf.constant([1, 2, 3], dtype=tf.int32)
unicode_strings = ints_to_unicode(strings)

print(unicode_strings)
