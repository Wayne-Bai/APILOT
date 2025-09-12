import tensorflow as tf

# Define a tensor of strings
string_tensor = tf.constant(["tensorflow", "machine learning", "deep learning"])

# Specify the start and end indices for the substrings
# Here, for example, extracting "tensor" from "tensorflow", "machine" from "machine learning", and "deep" from "deep learning"
start_indices = tf.constant([0, 0, 0])
end_indices = tf.constant([6, 7, 4])

# Use tf.strings.substr to extract substrings
substrings = tf.strings.substr(string_tensor, start_indices, end_indices - start_indices)

# Create a TensorFlow session to run the graph
# However, TensorFlow 2.x works eagerly by default, so we can just execute this in most environments.
substrings_result = substrings.numpy()

# Print the result
print(substrings_result)
