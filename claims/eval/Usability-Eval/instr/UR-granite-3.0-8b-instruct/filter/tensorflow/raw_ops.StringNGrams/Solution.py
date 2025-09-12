import tensorflow as tf

# Assuming you have a RaggedTensor `input_tensor` with string values
# Create a vocabulary from the strings in the input tensor
vocabulary = tf.strings.reduce_join(input_tensor)
vocabulary = tf.strings.split(vocabulary)
vocabulary = tf.unique(vocabulary)[0]

# Define the ngram size
ngram_size = 3

# Create ngrams from the input tensor
ngrams = tf.ragged.map_flat_values(
    lambda x: tf.strings.join(tf.unravel_index(tf.range(len(x) - ngram_size + 1), [ngram_size]))
    .numpy(),
    input_tensor
)

# Print the ngrams
print(ngrams)
