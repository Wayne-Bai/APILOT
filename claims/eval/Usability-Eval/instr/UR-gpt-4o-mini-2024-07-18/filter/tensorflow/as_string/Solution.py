import tensorflow as tf

# Sample tensor
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Function to convert tensor entries to strings
def convert_tensor_to_strings(input_tensor):
    return tf.strings.as_string(input_tensor)

# Convert the tensor
string_tensor = convert_tensor_to_strings(tensor)

# Print the result
tf.print(string_tensor)
