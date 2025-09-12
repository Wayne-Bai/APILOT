
import tensorflow as tf

input_data = tf.ragged.constant([["hello", "world", "how"], ["are", "you"]])
n = 2
separator = " "

ngram_data = tf.strings.join(input_data, separator)
ngrams = tf.strings.ngrams(ngram_data, n, separator)

print(ngrams)
