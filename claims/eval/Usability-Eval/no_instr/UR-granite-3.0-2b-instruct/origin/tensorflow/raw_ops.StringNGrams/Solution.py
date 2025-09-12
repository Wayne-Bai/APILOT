import tensorflow as tf

def create_ngrams(data, n):
    """
    Creates ngrams from ragged string data.

    Args:
    data (tf.RaggedTensor): The input ragged tensor of strings.
    n (int): The order of the ngrams.

    Returns:
    tf.RaggedTensor: The output ragged tensor of ngrams.
    """
    # Create a mapping from characters to ngrams
    char_to_ngram = tf.lookup.StaticVocabularyTable(
        tf.lookup.TextTable(
            table_id="char_to_ngram",
            table_gradient_check_all=False,
            num_oovs=1,
            oov_token="[OOV]",
            index=tf.range(n),
            output_dtype=tf.int64
        )
    )

    # Create a mapping from ngrams to characters
    ngram_to_char = tf.lookup.StaticVocabularyTable(
        tf.lookup.TextTable(
            table_id="ngram_to_char",
            table_gradient_check_all=False,
            num_oovs=1,
            oov_token="[OOV]",
            index=tf.range(n),
            output_dtype=tf.int64
        )
    )

    # Create a mapping from ngrams to their corresponding characters
    ngram_to_char_map = char_to_ngram.lookup(ngram_to_char.lookup(data.to_tensor()))

    # Create a new ragged tensor of ngrams
    ngrams = tf.ragged.map_rows(
        lambda x: tf.ragged.map(ngram_to_char_map, x),
        data
    )

    return ngrams
