
import tensorflow as tf

def encode_tensor_to_unicode_string(input_tensor):
    encoded_strings = tf.strings.unicode_encode(input_tensor, 'UTF-8')
    return encoded_strings

# Test
input_tensor = tf.constant([72, 101, 108, 108, 111], dtype=tf.int32)
result = encode_tensor_to_unicode_string(input_tensor)
print(result)
