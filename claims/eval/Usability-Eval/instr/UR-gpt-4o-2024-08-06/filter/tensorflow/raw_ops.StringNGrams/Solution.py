import tensorflow as tf

# Example ragged strings tensor
ragged_strings = tf.ragged.constant([
    ["This", "is", "an", "example", "sentence"],
    ["tensorflow", "creates", "ngrams"],
    ["practice", "makes", "perfect"]
])

# Parameters for ngrams
ngram_width = 2  # e.g., bigrams
separator = b" "  # separator between words in a ngram

# Creating the ngrams
ngrams = tf.raw_ops.StringNGrams(
    data=ragged_strings,
    separator=separator,
    ngram_widths=[ngram_width],
    left_pad="",
    right_pad="",
    pad_width=0
)

# Now `ngrams` is a tensor of ngrams
print(ngrams.to_list())
