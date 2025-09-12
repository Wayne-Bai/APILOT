import tensorflow as tf

def substring_from_tensor(tensor, start, length):
    substrings = tf.strings.substr(tensor, pos=start, len=length)
    return substrings

# Example tensor of strings
tensor_of_strings = tf.constant(["hello world", "tensorflow", "substring example"])
start_position = 6
substring_length = 5

# Get substrings
result = substring_from_tensor(tensor_of_strings, start_position, substring_length)
print(result)
