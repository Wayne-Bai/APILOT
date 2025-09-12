import tensorflow as tf

# Method in tf.raw_ops, Encode a tensor of ints into unicode strings.

# Create a tensor of ints
int_tensor = tf.constant([101, 107, 112, 111])

# Use tf.raw_ops.CStringV2 to encode the ints into unicode strings
unicode_strings = tf.raw_ops.CStringV2.decode_unicode_from_logits(int_tensor)

unicode_strings
