import tensorflow as tf

def create_ngrams_from_ragged_strings(ragged_tensor_strings, ngram_widths, separator=""):
    """
    Creates ngrams from a ragged tensor containing strings.

    Args:
    ragged_tensor_strings : tf.RaggedTensor
        A ragged tensor of strings.
    ngram_widths : list of ints
        Sizes of the ngrams to create.
    separator : str
        The separator to use when joining the strings in an ngram.

    Returns:
    tf.RaggedTensor
        A ragged tensor containing ngrams.
    """
    return tf.strings.ngrams(
        ragged_tensor_strings,
        ngram_widths=ngram_widths,
        separator=separator,
        pad_values='',
        preserve_short_sequences=True
    )

# Example usage:
ragged_tensor_input = tf.ragged.constant([["the", "quick", "brown", "fox"],
                                          ["jumps", "over", "the"],
                                          ["lazy", "dog"]])
ngram_widths = [2, 3]  # Create bigrams and trigrams

ngrams = create_ngrams_from_ragged_strings(ragged_tensor_input, ngram_widths)
print(ngrams)
