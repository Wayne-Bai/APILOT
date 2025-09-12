import tensorflow as tf

def convert_to_string(tensor):
    """
    Converts each entry in the given tensor to strings.
    
    Args:
    tensor: A Tensor of type string or numeric.
    
    Returns:
    A Tensor of type string.
    """
    
    # Use the tf.strings.as_string function to convert the tensor to string
    string_tensor = tf.strings.as_string(tensor)
    
    return string_tensor

# Example usage:
tensor = tf.constant([1, 2, 3, 4, 5])
print("Original Tensor: ", tensor)

# Convert the tensor to string
string_tensor = convert_to_string(tensor)
print("String Tensor: ", string_tensor)
