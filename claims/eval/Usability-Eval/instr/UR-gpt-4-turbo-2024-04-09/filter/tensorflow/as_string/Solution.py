import tensorflow as tf

def tensor_to_string(tensor):
    string_tensor = tf.strings.as_string(tensor)
    return string_tensor

# Example tensor
example_tensor = tf.constant([1, 2, 3, 4])
converted_tensor = tensor_to_string(example_tensor)

print(converted_tensor)
