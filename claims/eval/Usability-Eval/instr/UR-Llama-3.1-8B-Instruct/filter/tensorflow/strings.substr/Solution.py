import tensorflow as tf
import numpy as np

# Creating a tensor of strings
tensor_of_strings = tf.constant(['Hello', 'World', 'Tensorflow', 'Python'])

# Splitting the tensor into substrings of length 3
substrings = tf.strings.split(tensor_of_strings, sep='')

# Iterating over the substrings and updating them to return unrestricted size by using dynamic size
substring_start_index = tf.constant(0)
substring_size = tf.strings.length(tensor_of_strings[0])

substring = substrings[0][substring_start_index: substring_size]

for i in range(1, len(substrings)):
    # Extract substring of size based on the length i tensor string 
    substring += substrings[i]
    substring_size += tf.strings.length(substrings[i])
    
    if substring_size == tf.strings.length(tensor_of_strings[i]): 
        substring += ', '
        substring_start_index += tf.strings.length(substrings[i])
        substring_size = tf.strings.length(tensor_of_strings[i])

# Removing trailing and leading commas and spaces
substring = tf.strings.regex_replace(substring, r'^\s*,', '')
substring = tf.strings.regex_replace(substring, r',\s*$', '')

print(substring)
