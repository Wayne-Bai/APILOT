import tensorflow as tf

def get_substrings(strings, start, length):
    # strings is a tensor of strings
    # start is the starting index of the substring
    # length is the length of the substring

    substrings = tf.strings.substr(strings, start, length)
    return substrings

# Usage
strings = tf.constant(['hello', 'world'])
start = 1
length = 3
print(get_substrings(strings, start, length))
