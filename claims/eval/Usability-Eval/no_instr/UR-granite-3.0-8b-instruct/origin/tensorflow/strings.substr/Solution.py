import tensorflow as tf

# Let's assume we have a tensor of strings
strings_tensor = tf.constant(["hello", "world", "tensorflow"])

# To get substrings, we can use tf.strings.substr
# For example, to get the first 3 characters of each string
substrings = tf.strings.substr(strings_tensor, 0, 3)

# Print the substrings
print(substrings)
