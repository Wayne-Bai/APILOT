import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1, 2], [3, 4]])

# Convert the input tensor to a list of strings
string_list = input_tensor.to_list()

# Create a new tensor from the string list
output_tensor = tf.strings.bytes_to_numbers(string_list)

print(output_tensor)  # Output: [[1, 2], [3, 4]]
