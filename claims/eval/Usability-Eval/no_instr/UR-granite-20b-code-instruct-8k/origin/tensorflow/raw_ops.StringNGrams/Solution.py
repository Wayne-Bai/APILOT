import tensorflow as tf

def generate_ngrams(ragged_string_data, ngram_range):
  ngrams = tf.raw_ops.string_ngrams(input=ragged_string_data, ngram_width=ngram_range, separator=" ", reduction_type="UTF8_JOIN")
  return ngrams
