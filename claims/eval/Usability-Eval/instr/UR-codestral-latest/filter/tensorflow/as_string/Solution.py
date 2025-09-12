import tensorflow as tf

def tensor_to_string(tensor):
    return tf.strings.as_string(tensor)

# Example usage
tensor = tf.constant([1, 2, 3, 4, 5])
strings = tensor_to_string(tensor)
print(strings)
