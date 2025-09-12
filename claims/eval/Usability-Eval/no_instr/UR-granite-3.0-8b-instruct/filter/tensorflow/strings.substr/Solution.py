import tensorflow as tf

# Assuming you have a tensor of strings
strings_tensor = tf.constant(["hello", "world", "tensorflow"])

# To get substrings, you can use tf.strings.substr
# For example, to get the first 3 characters of each string
substring_tensor = tf.strings.substr(strings_tensor, 0, 3)

# Print the result
print(substring_tensor)
