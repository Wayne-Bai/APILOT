# Import required libraries
import tensorflow as tf

# Create a Tensor of strings
tensor_of_strings = tf.constant(["Hello, World!", "TensorFlow", "Machine Learning"])

# Create a Tensor of integers (indices)
indices = tf.constant([3, 6, 9])

# Create a Tensor of lengths for each string
string_lengths = tf.map_fn(lambda x: tf.shape(x)[0], tensor_of_strings)

# Mask to calculate substring
mask = tf.linalg.band_part(tf.ones((len(tensor_of_strings), len(tensor_of_strings[0]))), -1, 0) > indices

# Create a Tensor of offsets
offsets = tf.boolean_mask(tf.range(len(tensor_of_strings[0])), mask)

# Create a list to store substrings
substrings = []

# Iterate over each string in the tensor
for i, string in enumerate(tensor_of_strings):
    # Iterate over each offset
    substr = [string[j:j+1] for j in offsets[i:i+1]]
    substr = ''.join(substr)
    # Append substring to the list
    substrings.append(substr)

# Convert the list to a tensor
substrings = tf.constant(substrings)

# Print the tensor of substrings
print(substrings)
