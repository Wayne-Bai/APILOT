import tensorflow as tf

def tensor_to_strings(input_tensor):
    return tf.strings.to_string(input_tensor)

# Example usage:
input_tensor = tf.constant([1, 2, 3, 4, 5])
output_tensor = tensor_to_strings(input_tensor)
print(output_tensor)
