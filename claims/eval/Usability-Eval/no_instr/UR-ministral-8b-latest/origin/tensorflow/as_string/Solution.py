import tensorflow as tf

# Example tensor
input_tensor = tf.constant([1, 2, 3, 4, 5])

# Convert each entry in the tensor to a string
string_tensor = tf.strings/unicode_decode(input_tensor, 'UTF-8')

# Convert each entry back to a string
output_tensor = tf.strings/unicode_encode(tf.strings.bytes_to_text(string_tensor), 'UTF-8')

print(output_tensor)
