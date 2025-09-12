import tensorflow as tf

def create_ngrams(ragged_data, n):
    # Convert the ragged data into a dense tensor
    dense_data = tf.reshape(ragged_data, [-1])

    # Create the n-grams
    ngrams = tf.raw_ops.ngrams(dense_data, n)

    return ngrams

# Example usage
ragged_data = tf.constant([['hello', 'world'], ['tensor', 'flow']], dtype=tf.string)
n = 3
ngrams = create_ngrams(ragged_data, n)
