import tensorflow as tf

def get_substrings(input_tensor, start, end):
    """
    Returns substrings from a Tensor of strings.

    Args:
    input_tensor (tf.Tensor): A Tensor of strings.
    start (int): The starting index of the substring.
    end (int): The ending index of the substring.

    Returns:
    tf.Tensor: A Tensor containing the substrings.
    """
    return tf.strings.substr(input_tensor, start, end - start)

# Example usage:
input_strings = tf.constant(["Hello World", "TensorFlow", "Python Code"])
start_index = 0
end_index = 5

substrings = get_substrings(input_strings, start_index, end_index)
print(substrings)
