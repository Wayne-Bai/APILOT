import tensorflow as tf

def get_substrings(tensor, start, length):
    # Use tf.strings.substr to extract substrings from each element in the tensor
    substrings = tf.strings.substr(tensor, start, length)
    return substrings

# Example tensor of strings
tensor_of_strings = tf.constant(["Hello, World!", "TensorFlow", "2023"])

# Extract substrings starting at index 0 with length 5
substrings_output = get_substrings(tensor_of_strings, 0, 5)

# Run and print the result
tf.print(substrings_output)
