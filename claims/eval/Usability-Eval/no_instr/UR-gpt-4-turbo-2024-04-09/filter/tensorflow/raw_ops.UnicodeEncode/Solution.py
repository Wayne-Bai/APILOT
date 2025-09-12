import tensorflow as tf

def encode_ints_to_unicode(tensor):
    # Transforms a tensor of integers into encoded Unicode strings
    encoded_strings = tf.strings.unicode_encode(
        input=tensor,
        output_encoding='UTF-8'
    )
    return encoded_strings

# Example tensor of integers
int_tensor = tf.constant([[72, 101, 108, 108, 111], [87, 111, 114, 108, 100]])

# Encode integers to Unicode strings
encoded_unicode_strings = encode_ints_to_unicode(int_tensor)
print("Encoded Unicode Strings:\n", encoded_unicode_strings.numpy())
