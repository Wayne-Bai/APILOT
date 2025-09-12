import tensorflow as tf

# Sample data
strings = tf.constant(["Hello", "World", "TensorFlow"], dtype=tf.string)

# Function to get substring from a tensor of strings
def get_substring(strings, start, end):
    return tf.strings.substr(strings, start, end)

# Use the function to get substrings from the example data
substr_start = 1
substr_end = 3
substring_tensors = get_substring(strings, substr_start, substr_end)

# Print the substrings
for subs in substring_tensors:
    print(subs.numpy().decode())
