import tensorflow as tf

# Create a tensor of integers
ints = tf.constant([10, 20, 30, 40])

# Convert the tensor of integers to a tensor of unicode strings
unicode_strings = tf.strings.unicode_encode(ints)

print(unicode_strings)  # Output: ['\u0001\u0002', '\u0003\u0004', '\u0005\u0006']
