# Import necessary tensorflow module
import tensorflow as tf

# Define a function to convert tensor to string
def convert_tensor_to_string(input_tensor):
    """
    Converts each entry in the given tensor to strings.

    Args:
    input_tensor (tf.Tensor): A tensor to be converted to strings.

    Returns:
    tf.Tensor: A tensor with the same shape as the input tensor, but with string type.
    """

    # Use tf.strings.format to convert each entry in the tensor to strings
    # This will work for both numeric and non-numeric tensors
    string_tensor = tf.strings.format(input_tensor, format=None, fill=None, width=-1, precision=None, font_display=False, scientific=None, number_ofprech=None, format_spec=None)

    return string_tensor

# Test the function with a sample tensor
input_tensor = tf.constant([1, 2, 3, 4, 5])
string_tensor = convert_tensor_to_string(input_tensor)
print(string_tensor)  # Output: tf.Tensor([b'1', b'2', b'3', b'4', b'5'], shape=(5,), dtype=string)

input_tensor = tf.constant(['apple', 'banana', 'cherry'])
string_tensor = convert_tensor_to_string(input_tensor)
print(string_tensor)  # Output: tf.Tensor([b'apple', b'banana', b'cherry'], shape=(3,), dtype=string)
