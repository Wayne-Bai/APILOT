import tensorflow as tf

# Function to convert a tensor to string
def convert_tensor_to_string(tensor):
    # Ensure the input tensor is of type string
    string_tensor = tf.strings.as_string(tensor)
    return string_tensor

# Example usage
tensor = tf.constant([[1, 2], [3, 4]])
string_tensor = convert_tensor_to_string(tensor)

print(string_tensor)
