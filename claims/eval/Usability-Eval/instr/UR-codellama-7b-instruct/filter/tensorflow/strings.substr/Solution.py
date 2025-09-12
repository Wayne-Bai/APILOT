
import tensorflow as tf

def extract_substrings(input_tensor, window_size):
    """
    Extracts substrings from a Tensor of strings.

    Args:
        input_tensor (tf.Tensor): A Tensor of strings to be processed.
        window_size (int): The size of the sliding window to use for extracting substrings.

    Returns:
        tf.Tensor: A Tensor of substrings extracted from the input Tensor of strings.
    """
    # Create a placeholder for the input tensor
    input_placeholder = tf.placeholder(tf.string, shape=input_tensor.shape)

    # Convert the input tensor to a list of characters
    character_list = tf.strings.split(input_placeholder)

    # Initialize an empty Tensor to store the substrings
    substring_tensor = tf.zeros((0, window_size), dtype=tf.string)

    # Iterate over each element in the input tensor
    for i, _ in enumerate(input_tensor):
        # Get the current string
        current_string = input_tensor[i]

        # Create a list of all substrings with length <= window_size
        substrings = [current_string[j:j + window_size] for j in range(len(current_string))]

        # Add the substrings to the Tensor
        substring_tensor = tf.concat((substring_tensor, substrings), axis=0)

    return substring_tensor
