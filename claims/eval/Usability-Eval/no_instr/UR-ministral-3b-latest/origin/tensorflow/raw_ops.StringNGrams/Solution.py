import tensorflow.compat.v1 as tf

# Define the function to create ngrams from ragged string data
def create_ngrams(sentence, n):
    """
    Creates ngrams from a sentence.

    Args:
    - sentence (tf.Tensor): The input sentence.
    - n (int): The size of the ngrams.

    Returns:
    - ngrams (tf.Tensor): The generated ngrams.
    """
    # Convert the input sentence to a list of words
    words = tf.unstack(sentence)

    # Split the words into pairs
    pairs = [tf.map_fn(lambda x: (x, x), word) for word in words]

    # Concatenate the words using tf.raw_ops.concat_nd
    concatenated = tf.concat(list(pairs), axis=0)

    return concatenated

# Example usage
sentence = tf.constant(["Hello world", "This is a sentence"])
ngrams = create_ngrams(sentence, 2)
print(ngrams)
