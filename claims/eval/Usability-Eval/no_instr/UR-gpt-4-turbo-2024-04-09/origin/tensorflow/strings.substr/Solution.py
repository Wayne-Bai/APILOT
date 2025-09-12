import tensorflow as tf

def extract_substrings(tensor_strings, start, length):
    # Use tf.strings.substr to extract substrings
    substrings = tf.strings.substr(tensor_strings, pos=start, len=length)
    return substrings

# Example tensor of strings
tensor_strings = tf.constant(["hello world", "tensorflow", "substring example"])

# Example usage: Extract substrings starting at index 0 with length 5
result = extract_substrings(tensor_strings, 0, 5)
print(result)
