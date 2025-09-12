import tensorflow as tf

# Define a tensor of integers
integer_tensor = tf.constant([72, 101, 108, 108, 111], dtype=tf.int32)

# Define a function to encode integers to unicode strings using tf.raw_ops
def encode_ints_to_unicode(int_tensor, input_encoding='UTF-8', output_encoding='UTF-16-BE'):
    return tf.raw_ops.UnicodeEncode(
        input_values=int_tensor,
        input_encoding=input_encoding,
        output_encoding=output_encoding)

# Encode the integer tensor into unicode strings
encoded_unicode_tensor = encode_ints_to_unicode(integer_tensor)

# Run the session to get the output
print(f'Encoded Unicode Tensor: {encoded_unicode_tensor}')
