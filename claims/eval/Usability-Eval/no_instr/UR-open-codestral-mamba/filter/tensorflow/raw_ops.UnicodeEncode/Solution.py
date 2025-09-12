import tensorflow as tf
import numpy as np

# We will create a list of integers corresponding to Unicode characters
# These Unicode characters do not form a meaningful message, they are just for demonstration purposes.
unicode_chars = [65, 66, 67, 68, 69]

# Convert the list to a tensor
tensor_unicode_chars = tf.convert_to_tensor(unicode_chars, dtype=tf.int32)

# Encode the tensor of integers into Unicode strings
unicode_tensor_chars = tf.raw_ops.DecodeRaw(input=tensor_unicode_chars, Tout=tf.string)

print(unicode_tensor_chars.numpy())
