
import tensorflow as tf

ragged_data = tf.ragged.constant([['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h', 'i']])
ngrams = tf.raw_ops.NgramOp(
    data=ragged_data,
    ngram_limits=[1, 2],
    separator=' ',
    axis=1,
    output_shape=[ragged_data.shape[0], None]
)

with tf.Session() as sess:
    print(sess.run(ngrams))
