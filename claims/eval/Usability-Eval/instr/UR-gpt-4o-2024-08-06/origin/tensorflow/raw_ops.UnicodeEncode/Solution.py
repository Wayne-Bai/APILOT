import tensorflow as tf

# Sample tensor of integers
integer_tensor = tf.constant([[72, 101, 108, 108, 111], [87, 111, 114, 108, 100]])

def ints_to_unicode(int_tensor):
    # Convert each integer in the tensor to a character, forming strings
    unicode_strings = tf.strings.unicode_encode(int_tensor, output_encoding='UTF-8')
    return unicode_strings

# Encode the integer tensor to unicode strings
encoded_unicode_strings = ints_to_unicode(integer_tensor)

# Start a TensorFlow session and run the graph to get the result
# Note: In TensorFlow 2.x, eager execution is enabled by default
# so we don't need to create a session explicitly.

# Check the result
print(encoded_unicode_strings.numpy())  # Output will be: [b'Hello' b'World']
