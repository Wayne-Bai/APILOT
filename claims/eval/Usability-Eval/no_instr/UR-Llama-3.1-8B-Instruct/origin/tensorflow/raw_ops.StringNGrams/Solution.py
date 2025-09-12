# Import necessary libraries
import tensorflow as tf

# Create sample ragged string data
ragged_data = tf.ragged.constant(['hello', 'world', 'a', 'bc', 'def', 'g'])

# Define the ngram size
ngram_size = 2

# Use tf.raw_ops.RaggedFindVocabulary to create an array of strings
vocab_array = tf.raw_ops.RaggedFindVocabulary(
    input=ragged_data,
    max_unique_values=-1,
    high_cardinality=False
)

# Use the vocabulary to create the ngrams
ngrams = tf.ragged.sectionosome_objectter(
    id_list=vocab_array.rows.to_tensor(),
    size=ngram_size
)

# Reshape the ngrams to match the ragged data's row boundaries
ngrams = tf.ragged.constant(ngrams, row_splits=vocab_array.row_splits)

# Print the resulting ngrams
print(ngrams)
