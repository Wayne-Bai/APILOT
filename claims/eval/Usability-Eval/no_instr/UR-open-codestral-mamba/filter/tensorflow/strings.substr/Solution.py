import tensorflow as tf

def get_substrings(strings):
    return tf.strings.split(strings, sep=' ')

# Example usage:
# Here 'Tensor of Strings' refers to a Tensor of sentences. Each sentence is a string, and we want to split each sentence into words.
tensor_of_strings = tf.constant(['Hello World', 'AI is the future', 'Python is cool'])
substrings = get_substrings(tensor_of_strings)
print(substrings.numpy())
