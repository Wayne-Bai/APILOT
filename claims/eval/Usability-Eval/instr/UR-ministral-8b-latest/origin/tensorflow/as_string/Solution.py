import tensorflow as tf

# Assume 'input_tensor' is the given tensor
input_tensor = tf.constant([123, 456, 789], dtype=tf.int32)

# Convert each entry in the tensor to strings
strings_tensor = tf.strings.unicode_decode(input_tensor, 'UTF-8')
strings_tensor_decoded = tf.strings.unicode_encode(strings_tensor, 'UTF-8')

# Print the result
print(strings_tensor_decoded)
