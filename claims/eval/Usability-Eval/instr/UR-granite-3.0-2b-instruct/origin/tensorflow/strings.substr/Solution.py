import tensorflow as tf

# Create a tensor of strings
tensor_of_strings = tf.constant(["Hello", "World", "TensorFlow"])

# Define a function to return substrings
def get_substrings(tensor):
    substrings = []
    for string in tensor:
        for i in range(len(string)):
            for j in range(i+1, len(string)+1):
                substrings.append(string[i:j])
    return substrings

# Get substrings from the tensor
substrings = get_substrings(tensor_of_strings)

# Print the substrings
for substring in substrings:
    print(substring)
