
import tensorflow as tf

# Define the input tensor of ints
input_tensor = tf.constant([104, 101, 108, 108, 111], dtype=tf.int32)

# Encode the tensor of ints into unicode strings using tf.strings.unicode_encode
unicode_strings = tf.strings.unicode_encode(input_tensor, input_encoding='UTF-8')

print(unicode_strings)
