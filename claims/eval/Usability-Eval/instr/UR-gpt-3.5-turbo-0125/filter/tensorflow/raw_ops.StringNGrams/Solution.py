
import tensorflow as tf

def create_ngrams(data, n):
    ngrams = tf.strings.ngrams(data, n, separator=' ', pad_values='', left_pad=False)
    return ngrams

# Example Usage
data = tf.ragged.constant([['I', 'love', 'coding'], ['Machine', 'learning']])
ngrams = create_ngrams(data, 2)
print(ngrams)
