
import tensorflow as tf

def create_ngrams(data, n):
    ngrams = tf.raw_ops.StringNGrams(data=data, n=n)
    return ngrams

# Example usage
data = tf.ragged.constant([["apple", "banana", "cherry"], ["orange", "grape"]])
n = 2
ngrams = create_ngrams(data, n)
print(ngrams)
