
import tensorflow as tf

# Create a tensor of strings
strings = tf.constant(["Hello", "World", "TensorFlow"])

# Define a function to return substrings from the tensor
def get_substrings(tensor, start, length):
    return tf.strings.substr(tensor, start, length)

# Call the function with start index 1 and length 2
substrings = get_substrings(strings, 1, 2)

# Print the result
print(substrings.numpy())
