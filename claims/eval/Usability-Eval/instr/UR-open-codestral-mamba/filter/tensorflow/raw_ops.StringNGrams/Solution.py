import tensorflow as tf

def ngrams(inputs, n):
    """
    Create ngrans from a 1D tensor of strings
    """
    # split the strings into individual characters
    chars = tf.strings.unicode_split(inputs, "UTF-8")

    # create ngrams
    return tf.sequence_candidates(chars, n)

# test the function
sentences = tf.constant(["hello world", "hi how are you"])
ngrams_2 = ngrams(sentences, 2)

ngrams_2
