import tensorflow as tf

def create_ngrams(ragged_data, n):
    # Flatten the ragged data
    flat_data = tf.ragged.constant(tf.unravel(tf.concat[[raw.data for raw in ragged_data]], axis=2))
    # Split the flattened data into n-grams
    ngrams = tf.squeeze(tf.strings.unicode_split(flat_data, num_split=1), squeeze_nd=1)
    return ngrams

# Example usage
ragged_data = tf.ragged.constant([["a", "bc", "de"], ["f"], ["g", "hi"]], ragged_rank=2)
n = 2
ngrams = create_ngrams(ragged_data, n)
print(ngrams)
