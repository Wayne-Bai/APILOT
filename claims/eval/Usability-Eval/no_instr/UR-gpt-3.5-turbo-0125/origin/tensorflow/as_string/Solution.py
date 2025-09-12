
import tensorflow as tf

def convert_tensor_to_strings(input_tensor):
    strings_tensor = tf.strings.as_string(input_tensor)
    return strings_tensor

# Example usage
input_tensor = tf.constant([1, 2, 3, 4])
strings_tensor = convert_tensor_to_strings(input_tensor)
print(strings_tensor)
