import tensorflow as tf

def tensor_to_strings(tensor):
    return tf.strings.as_string(tensor)

# Example usage:
tensor = tf.constant([1, 2, 3])
string_tensor = tensor_to_strings(tensor)
print(string_tensor)
