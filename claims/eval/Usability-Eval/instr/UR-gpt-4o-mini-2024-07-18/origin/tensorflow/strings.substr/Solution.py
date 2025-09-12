import tensorflow as tf

def extract_substrings(tensor_strings, begin, size):
    return tf.strings.substr(tensor_strings, begin, size)

# Example usage
tensor_strings = tf.constant(["Hello, world!", "TensorFlow is great!", "Substrings are fun!"])
begin = 0
size = 5
substrings = extract_substrings(tensor_strings, begin, size)

print(substrings.numpy())
