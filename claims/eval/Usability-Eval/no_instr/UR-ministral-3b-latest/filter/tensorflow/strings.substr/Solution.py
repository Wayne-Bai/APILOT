import tensorflow as tf

# Assuming the input tensor is `strings_tensor`
strings_tensor = tf.constant(["Hello World", "Python Coding", "AI and Machine Learning"])

# Using tf.strings.split method to split the strings and selecting every second element (index 1)
substrings_tensor = tf.strings.split(strings_tensor, keep_right_discard_right=True)

print(substrings_tensor)
