import tensorflow as tf

# Dummy input tensor
input_tensor = tf.constant([1, 2, 3, 4, 5])

# Convert each entry in the input tensor to strings
string_tensor = tf.strings.unicode_decode(input_tensor, 'UTF-8')

string_tensor
