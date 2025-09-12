
import tensorflow as tf

# Assume `tensor` is your tensor to be converted to strings.
tensor = tf.constant([[1, 2], [3, 4]])
string_tensor = tf.strings.as_string(tensor)

print(string_tensor)
