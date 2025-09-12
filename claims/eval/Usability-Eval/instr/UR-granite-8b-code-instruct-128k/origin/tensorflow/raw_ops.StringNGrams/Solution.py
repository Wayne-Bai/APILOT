import tensorflow as tf

ragged_data = tf.ragged.constant([[b"a", b"bc"], [b"ab", b"c", b""], [b"abc", b""]])
ngrams = tf.raw_ops.RaggedNGrams(
    data=ragged_data,
    ngram_counts=[1, 2],
    separator=b" ",
    pad_string=b"",
    preserve_weights=False,
    output_type=tf.string,
)

with tf.Session() as sess:
    print(sess.run(ngrams))
