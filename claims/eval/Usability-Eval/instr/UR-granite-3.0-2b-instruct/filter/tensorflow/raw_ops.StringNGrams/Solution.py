import tensorflow as tf

# Create a ragged tensor
data = tf.ragged.constant([
    tf.constant(["Hello", "world"]),
    tf.constant(["This", "is", "a", "test"]),
    tf.constant(["of", "the", "emergency", "system"])
])

# Define the n-gram size
ngram_size = 2

# Create n-grams
ngrams = tf.raw_ops.RaggedNgrams(
    data,
    ngram_size,
    n=tf.size(data, out_type=tf.int32),
    output_type=tf.string
)

# Print the n-grams
with tf.Session() as sess:
    print(sess.run(ngrams))
