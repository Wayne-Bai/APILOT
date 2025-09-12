import tensorflow as tf

def extract_substrings(tensor, start, length):
    """
    Extract substrings from a tensor of strings.

    Parameters:
    tensor (tf.Tensor): A tensor containing strings.
    start (int): The starting index for the substring extraction.
    length (int): The length of the substring to extract.

    Returns:
    tf.Tensor: A tensor containing the extracted substrings.
    """
    return tf.strings.substr(tensor, start, length)

# Example usage
string_tensor = tf.constant(["Hello, World!", "TensorFlow is great!", "OpenAI makes coding easier."])
start_index = 0
substring_length = 5

result = extract_substrings(string_tensor, start_index, substring_length)
print(result.numpy())
