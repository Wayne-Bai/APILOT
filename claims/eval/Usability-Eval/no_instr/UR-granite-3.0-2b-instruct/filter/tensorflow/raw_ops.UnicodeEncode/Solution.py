import tensorflow as tf

def encode_int_to_unicode(input_tensor):
    # Create a lookup table for integer to Unicode mapping
    lookup_table = tf.lookup.StaticHashTable(
        tf.lookup.KeyValueTensorInitializer(
            keys=tf.range(tf.size(tf.unique_ints64(input_tensor))),
            values=tf.cast(tf.unique_ints64(input_tensor), tf.string),
            key_dtype=tf.int64,
            value_dtype=tf.string
        ),
        default_value=tf.string.empty()
    )

    # Encode the input tensor
    encoded_tensor = lookup_table.lookup(input_tensor)

    return encoded_tensor

# Example usage:
input_tensor = tf.constant([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4])
encoded_tensor = encode_int_to_unicode(input_tensor)
print(encoded_tensor)
