import tensorflow as tf

# Example of ragged string data
ragged_strings = tf.ragged.constant([
    ["the quick", "brown fox"],
    ["jumps", "over the", "lazy dog"],
    ["hello", "world"]
])

# Create ngrams from the ragged string data
# Here we are using n=2 for bigrams, adjust `n` as needed
n = 2
ngrams = tf.strings.ngrams(ragged_strings, n)

# To examine the output
print(ngrams)
