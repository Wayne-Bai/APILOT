import tensorflow as tf

def return_substrings(tensor_strings, start, size):
    substrings = tf.strings.substr(tensor_strings, start, size)
    return substrings

# Example usage
tensor_strings = tf.constant(["Hello, World!", "TensorFlow is great", "Python is amazing"])
start_index = 0
substring_size = 5

result = return_substrings(tensor_strings, start_index, substring_size)
print(result.numpy())  # Output: [b'Hello' b'Tens' b'Pytho']
