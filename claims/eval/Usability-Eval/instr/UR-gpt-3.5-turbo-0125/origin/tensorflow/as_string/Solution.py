
import tensorflow as tf

def convert_tensor_to_strings(input_tensor):
    # Convert each entry in the tensor to strings
    strings_tensor = tf.strings.as_string(input_tensor)
    
    return strings_tensor

# Test the function
input_tensor = tf.constant([12, 34, 56])
strings_tensor = convert_tensor_to_strings(input_tensor)
print(strings_tensor)
