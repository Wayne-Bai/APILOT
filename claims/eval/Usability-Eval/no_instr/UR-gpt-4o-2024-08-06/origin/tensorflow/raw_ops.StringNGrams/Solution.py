import tensorflow as tf

# Define some example string data as a ragged tensor
ragged_strings = tf.ragged.constant([['hello', 'world'], ['tensorflow', 'is', 'great'], ['python', 'coding']])

# Parameters for ngrams creation
# ngram_widths: The sizes of the ngrams to create; in this case, we want bigrams (width of 2)
# We can create multiple sizes too, by passing a list, e.g., [2, 3] for bigrams and trigrams
ngram_widths = [2]
separator = ' ' # The separator to use while joining ngrams
pad_values = None  # None means no padding; otherwise, use something like ['', '']

# Extract ngrams from the ragged tensor of strings
ngrams = tf.ragged.map_flat_values(
    tf.strings.ngrams,
    ragged_strings,
    ngram_widths=ngram_widths,
    separator=separator,
    pad_values=pad_values
)

# Evaluate and print the ngrams
tf.print(ngrams)
