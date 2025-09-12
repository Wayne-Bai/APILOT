import tensorflow as tf

# Assuming you have a RaggedTensor of strings
input_tensor = tf.ragged.constant([['this', 'is', 'a', 'test'], ['another', 'example']])

# Define the ngram size
ngram_size = 2

# Create ngrams
ngrams = tf.raw_ops.CreateNGrams(
    input=input_tensor,
    ngram_sizes=[ngram_size],
    separate_prefix_and_suffix=True,
    name=None
)

# Print the ngrams
print(ngrams)
