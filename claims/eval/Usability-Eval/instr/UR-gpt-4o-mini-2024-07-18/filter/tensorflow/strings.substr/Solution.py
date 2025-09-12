import tensorflow as tf

def extract_substrings(tensor_of_strings, start, size):
    # Use tf.strings.substr to extract substrings from the input tensor
    return tf.strings.substr(tensor_of_strings, start, size)

# Example usage
tensor_of_strings = tf.constant(["hello", "world", "tensorflow"])
start = 1
size = 3

substrings = extract_substrings(tensor_of_strings, start, size)
print(substrings.numpy())
