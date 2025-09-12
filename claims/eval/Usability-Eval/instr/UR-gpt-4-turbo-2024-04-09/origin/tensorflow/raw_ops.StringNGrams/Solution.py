import tensorflow as tf

def create_ngrams_from_ragged_strings(values, ngram_widths, separator, ragged_rank=1):
    """
    Creates ngrams from ragged string data.

    Args:
    values (list of strings): The strings from which to form ngrams.
    ngram_widths (list of int): The sizes of ngrams to create.
    separator (str): The separator to use when joining strings into ngrams.
    ragged_rank (int, optional): The ragged rank of the tensor if the input isn't already a ragged tensor. Default is 1.

    Returns:
    tf.RaggedTensor: Ragged tensor containing the ngrams.
    """
    # Create a RaggedTensor from the input values
    if isinstance(values, tf.RaggedTensor):
        ragged_tensor_input = values
    else:
        ragged_tensor_input = tf.ragged.constant(values, ragged_rank=ragged_rank)
    
    # Use the strings_ngrams operation to generate ngrams
    ngrams = tf.strings.ngrams(
        ragged_tensor_input,
        ngram_widths=ngram_widths,
        separator=separator
    )
    
    return ngrams

# Example usage:
input_strings = [["hello", "world"], ["tensorflow", "is", "great"], ["enjoy", "learning"]]
ngram_widths = [2]
separator = " "
ragged_tensor_ngrams = create_ngrams_from_ragged_strings(input_strings, ngram_widths, separator)
print(ragged_tensor_ngrams)
