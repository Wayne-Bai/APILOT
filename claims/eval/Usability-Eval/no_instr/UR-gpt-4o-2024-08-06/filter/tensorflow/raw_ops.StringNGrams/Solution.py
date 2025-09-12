import tensorflow as tf

def create_ngrams(ragged_strings, ngram_size, separator=" "):
    """
    Creates ngrams from ragged string data.
    
    Parameters:
    ragged_strings (tf.ragged.RaggedTensor): Input ragged tensor of strings.
    ngram_size (int): The size of ngrams to create.
    separator (str): The separator used to join ngrams.

    Returns:
    tf.ragged.RaggedTensor: A ragged tensor of ngrams.
    """
    def generate_ngrams(words):
        ngrams = []
        for i in range(len(words) - ngram_size + 1):
            ngram = separator.join(words[i:i + ngram_size])
            ngrams.append(ngram)
        return ngrams
    
    ngrams = ragged_strings.with_flat_values(tf.strings.split(ragged_strings.flat_values))
    ngrams = ngrams.with_flat_values(
        tf.ragged.map_flat_values(generate_ngrams, ngrams.flat_values)
    )
    
    return ngrams

# Example usage
ragged_strings = tf.ragged.constant(["the quick brown fox", "jumps over the lazy dog"])
ngrams = create_ngrams(ragged_strings, ngram_size=2)
print(ngrams)
