import tensorflow as tf

# Define a tensor of integers (for example, Unicode code points for some characters)
int_tensor = tf.constant([[72, 101, 108, 108, 111], [87, 111, 114, 108, 100]], dtype=tf.int32)

# Use tf.strings.unicode_encode to convert ints to unicode strings
batch_unicode_strings = tf.strings.unicode_encode(int_tensor, output_encoding='UTF-8')

# Evaluate the tensors to see the output
print(batch_unicode_strings.numpy())  # Expected output: [b'Hello', b'World']
