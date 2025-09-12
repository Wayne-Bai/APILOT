
import tensorflow as tf

def convert_tensor_to_strings(input_tensor):
    string_tensor = tf.strings.as_string(input_tensor)
    return string_tensor

# Example usage
input_tensor = tf.constant([1, 2, 3, 4, 5])
result = convert_tensor_to_strings(input_tensor)
print(result)
