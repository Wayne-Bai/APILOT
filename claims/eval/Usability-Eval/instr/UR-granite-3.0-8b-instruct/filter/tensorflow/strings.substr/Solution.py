import tensorflow as tf

# Assuming tf_strings is a tensor of strings
tf_strings = tf.constant(["Hello", "World", "Tensorflow", "is", "awesome"])

# Define the start and end indices for the substring
start_index = tf.constant(1)
end_index = tf.constant(4)

# Use tf.strings.substr to extract the substring
substring = tf.strings.substr(tf_strings, start_index, end_index)

# Print the result
print(substring)
