import tensorflow as tf

tensor_of_strings = tf.constant(['Hello', 'World'])
substrings = tf.strings.substr(tensor_of_strings, 1, 2)

print(substrings.numpy()) # ['el' 'or']
