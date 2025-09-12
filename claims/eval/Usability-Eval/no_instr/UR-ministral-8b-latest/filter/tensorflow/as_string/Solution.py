import tensorflow as tf

# Assumption: input_tensor is your input tensor
input_tensor = tf.constant([1, 2, 3, 4, 5])

# Convert each entry in the tensor to strings
str_tensor = tf.strings.unicode_decode(input_tensor, 'UTF-8')

# If the tensor contains integers, you can process the data accordingly
# Suppose you want to convert each integer to its string representation
string_tensor = tf.strings.unicode_encode(str_tensor, 'UTF-8')

print(string_tensor)
