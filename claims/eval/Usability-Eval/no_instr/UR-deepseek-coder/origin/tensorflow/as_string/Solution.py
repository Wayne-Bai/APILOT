import tensorflow as tf

def tensor_to_strings(tensor):
    # Convert each element in the tensor to a string
    string_tensor = tf.strings.as_string(tensor)
    return string_tensor

# Example usage:
tensor = tf.constant([1.0, 2.0, 3.0])
result = tensor_to_strings(tensor)
print(result.numpy())
