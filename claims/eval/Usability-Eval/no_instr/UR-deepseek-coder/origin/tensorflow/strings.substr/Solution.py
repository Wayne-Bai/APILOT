import tensorflow as tf

def extract_substrings(input_tensor, start_indices, lengths):
    """
    Extracts substrings from a Tensor of strings.

    Args:
    input_tensor: A Tensor of dtype string.
    start_indices: A Tensor of dtype int32 or int64, indicating the starting indices of the substrings.
    lengths: A Tensor of dtype int32 or int64, indicating the lengths of the substrings.

    Returns:
    A Tensor of dtype string containing the extracted substrings.
    """
    # Convert input tensor to RaggedTensor to handle variable-length strings
    input_ragged = tf.strings.unicode_split(input_tensor, 'UTF-8')
    
    # Create a mask for the substrings
    mask = tf.sequence_mask(lengths, maxlen=tf.reduce_max(lengths))
    
    # Apply the mask to extract the substrings
    substrings_ragged = tf.ragged.boolean_mask(input_ragged, mask)
    
    # Convert RaggedTensor back to dense tensor
    substrings = substrings_ragged.to_tensor(default_value='')
    
    return substrings

# Example usage:
input_strings = tf.constant(['hello', 'world', 'tensorflow'])
start_indices = tf.constant([1, 2, 3], dtype=tf.int32)
lengths = tf.constant([2, 3, 4], dtype=tf.int32)

substrings = extract_substrings(input_strings, start_indices, lengths)
print(substrings.numpy())
