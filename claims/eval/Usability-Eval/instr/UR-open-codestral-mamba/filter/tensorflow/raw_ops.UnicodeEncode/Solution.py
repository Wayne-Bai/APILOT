import tensorflow as tf

# Convert tensor of integers to Unicode strings

# Example data
input_tensor = tf.constant([65, 66, 67, 68, 69], dtype=tf.int32)

# Convert integers to Unicode strings
unicode_strings = tf.raw_ops.DecodeRaw(input=input_tensor, little_endian=False, out_type=tf.uint8)

# Print the Unicode strings
print(unicode_strings)
