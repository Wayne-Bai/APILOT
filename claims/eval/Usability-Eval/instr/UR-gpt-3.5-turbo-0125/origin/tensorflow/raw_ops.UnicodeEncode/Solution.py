
import tensorflow as tf

# Define input tensor containing integers
input_tensor = tf.constant([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100])

# Convert integers into unicode strings
unicode_strings = tf.strings.unicode_encode(input_tensor, "UTF-8")

print(unicode_strings)
