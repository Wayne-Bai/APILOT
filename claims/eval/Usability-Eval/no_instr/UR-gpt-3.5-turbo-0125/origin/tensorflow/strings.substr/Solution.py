
import tensorflow as tf

# Define a tensor of strings
strings = tf.constant(['hello', 'world', 'tensorflow', 'python'])

# Extract substrings
substring = tf.strings.substr(strings, pos=0, len=4)

print(substring)
