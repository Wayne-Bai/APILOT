import tensorflow as tf

# Potential input data as a ragged tensor
ragged_data = tf.ragged.constant([["A", "B", "C"], ["D", "E", "F"], ["G", "H"]])

# Define the ngram size (you can modify this value)
ngram_size = 2

# Generate ngrams from the ragged data
ngrams = tf.strings.ngrams(ragged_data, ngram_size)

# Reshape and join ngrams to convert them into string
ngrams_str = tf.strings.reduce_join(ngrams, separator=' ')

print(ngrams_str)
