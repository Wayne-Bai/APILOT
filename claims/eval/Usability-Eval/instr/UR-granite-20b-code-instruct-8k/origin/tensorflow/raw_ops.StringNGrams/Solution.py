
import tensorflow as tf
data = tf.constant(['This', 'is', 'a', 'test'])
ngrams, _, weights = tf.raw_ops.string_ngrams(data,
ngram_width=2,
weights=[0.5, 0.25, 0.125, 0.125],
left_pad='replicate',
right_pad='replicate',
pad_value='')
print(ngrams.numpy())
