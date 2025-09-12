import tensorflow as tf

def convert_tensor_to_strings(tensor):
    string_tensor = tf.strings.as_string(tensor)
    return string_tensor

# Example usage:
example_tensor = tf.constant([1, 2, 3, 4])
converted_tensor = convert_tensor_to_strings(example_tensor)
print(converted_tensor)
