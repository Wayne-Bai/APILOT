import tensorflow as tf
from tensorflow.ragged import ragged_string_ops as ragged_string_ops

ragged_strings = tf.ragged.constant([['This', 'is', 'a', 'test', 'string'], ['This', 'is', 'another', 'test', 'string'], ['This', 'is', 'a', 'third', 'test', 'string']])
ragged_strings = ragged_string_ops.to_unicode(ragged_strings)

def ngrams_from_ragged_strings(ragged_strings, n):
    ngrams = []
    for i in range(ragged_strings.shape[0]):
        for j in range(ragged_strings.shape[1] - n + 1):
            ngrams.append(ragged_strings[i, j:j+n])
    return tf.ragged.stack(ngrams)

result = ngrams_from_ragged_strings(ragged_strings, 3)
print(result)
