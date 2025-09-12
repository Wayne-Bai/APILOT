import tensorflow as tf

# Create a tensor of integers representing Unicode code points
ints_tensor = tf.constant([65, 66, 67])  # Unicode for 'A', 'B', 'C'

# Encode the tensor of ints into Unicode strings
unicode_strings = tf.strings.encode_base_eight(ints_tensor)

# If you want to print the result
print(unicode_strings.numpy())
