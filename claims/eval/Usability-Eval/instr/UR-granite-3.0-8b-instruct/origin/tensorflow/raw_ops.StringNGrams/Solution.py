import tensorflow as tf
from tensorflow.python.ops.ragged import ragged_factory_ops

def create_ngrams(ragged_input, n, delimiter=' '):
    """
    Creates ngrams from ragged string data.

    Args:
    ragged_input: A RaggedTensor containing the input strings.
    n: The size of the ngrams to create.
    delimiter: The delimiter used to split the input strings into words.

    Returns:
    A RaggedTensor containing the ngrams.
    """
    # Split the input strings into words using the delimiter.
    words = tf.strings.split(ragged_input, delimiter)

    # Create ngrams from the words.
    ngrams = ragged_factory_ops.constant_value(
        [list(range(i, i + n)) for i in range(len(words) - n + 1)],
        ragged_rank=1,
        inner_shape=(),
        dtype=tf.int64)

    ngrams = tf.gather(words, ngrams)

    # Flatten the ngrams into a 1D tensor.
    ngrams = tf.reshape(ngrams, [-1])

    return ngrams
