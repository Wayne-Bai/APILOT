import tensorflow as tf

def encode_int_to_unicode(input_data):
    """
    Encode a tensor of ints into unicode strings.

    Args:
    input_data (tensor): A tensor of integers to be encoded.

    Returns:
    tensor: A tensor of unicode strings.
    """

    # Ensure input is a tensor
    input_data = tf.convert_to_tensor(input_data)

    # Use the tf.strings.encode() method to encode the tensor of ints into unicode strings
    encoded_data = tf.strings.encode(input_data, 'unicode', errors='ignore')

    return encoded_data

# Example usage:
input_values = tf.constant([104, 101, 108, 108, 111])
encoded_values = encode_int_to_unicode(input_values)

# Decode the unicode values back to string for printing
decoded_values = tf.strings.unicode_decode(encoded_values, 'utf-8')

print(decoded_values)
