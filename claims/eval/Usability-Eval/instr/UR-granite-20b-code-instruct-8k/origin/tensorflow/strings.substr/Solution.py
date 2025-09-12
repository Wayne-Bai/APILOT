import tensorflow as tf

# Define input tensor
input_tensor = tf.constant(['Hello', 'World', 'TensorFlow', ' rocks!'])

# Define start and end indices for substrings
start_index = tf.constant([0, 1, 0, 4])
end_index = tf.constant([5, 5, 10, 9])

# Usetf.strings.substr to extract substrings
output_tensor = tf.strings.substr(input_tensor, start_index, end_index - start_index)

# Print the output tensor
print(output_tensor)
