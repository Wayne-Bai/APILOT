import tensorflow as tf

# Define a tensor of strings
string_tensor = tf.constant(["tensorflow", "machine", "learning", "example"])

# Parameters for substrings: start index and length of substrings to extract
start_offsets = tf.constant([0, 1, 2, 3])
lengths = tf.constant([3, 3, 3, 3])

# Extract substrings using tf.strings.substr
substrings = tf.strings.substr(input=string_tensor, pos=start_offsets, len=lengths)

# Execute the TensorFlow session to evaluate the substrings
print(substrings.numpy())
