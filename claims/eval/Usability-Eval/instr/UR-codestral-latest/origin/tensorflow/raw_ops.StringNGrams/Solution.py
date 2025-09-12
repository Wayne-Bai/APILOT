import tensorflow as tf

# Assume 'data' is a tf.RaggedTensor of strings
data = tf.ragged.constant([["Hello", "world!"], ["Goodbye"]])

def create_ngrams(x, n):
    # Convert each word into a sequence of character n-grams
    ngrams = tf.strings.ngrams(x, n, separator=" ", pad_width=None)
    return ngrams

n = 2  # for bi-grams
ngrams_data = tf.ragged.map_flat_values(create_ngrams, data, n)
print(ngrams_data)
