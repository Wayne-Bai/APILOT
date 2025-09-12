
import tensorflow as tf

# Define the input strings
input_strings = ["this", "is", "a", "test"]

# Create a ragged tensor from the input strings
ragged_string = tf.ragged.constant(input_strings)

# Specify the ngram size and skip size
ngram_size = 2
skip_size = 1

# Use the raw_ops method to create ngrams from the ragged tensor
ngrams = tf.raw_ops.RaggedNgrams(
    values=ragged_string,
    row_splits=ragged_string.row_lengths(),
    ngram_size=ngram_size,
    skip_size=skip_size
)

# Print the resulting ngrams
print(ngrams)
