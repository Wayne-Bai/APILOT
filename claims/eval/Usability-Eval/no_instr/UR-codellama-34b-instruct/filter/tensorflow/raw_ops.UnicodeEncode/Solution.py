import tensorflow as tf

# Define a tensor of integers
int_tensor = tf.constant([1, 2, 3, 4], dtype=tf.int64)

# Encode the integer tensor into Unicode strings
unicode_strings = tf.raw_ops.Encode(int_tensor, encoding='utf-8')

# Print the encoded Unicode strings
print(unicode_strings)
