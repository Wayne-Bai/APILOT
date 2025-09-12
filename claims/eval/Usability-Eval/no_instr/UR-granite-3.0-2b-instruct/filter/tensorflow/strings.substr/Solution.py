import tensorflow as tf

# Create a tensor of strings
tensor_of_strings = tf.constant(["Hello", "World", "TensorFlow", "Python"])

# Define a function to return substrings
def get_substrings(tensor, length):
    substrings = []
    for string in tensor:
        for i in range(len(string) - length + 1):
            substrings.append(string[i:i+length])
    return substrings

# Get substrings of length 3
substrings = get_substrings(tensor_of_strings, 3)

# Print the substrings
print(substrings)
