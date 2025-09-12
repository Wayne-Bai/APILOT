
import tensorflow as tf

# Define the input tensor of strings
input_strings = tf.constant(["hello", "world", "tensorflow", "substring"])

# Create a function that returns substrings from the tensor of strings
def get_substrings(input_strings, start_index, end_index):
    substrings = tf.strings.substr(input_strings, start_index, end_index - start_index)
    return substrings

# Define the start and end indices for substring extraction
start_index = 1
end_index = 4

# Call the function to get substrings from the input tensor
result_substrings = get_substrings(input_strings, start_index, end_index)

# Print the resulting substrings
print(result_substrings)
