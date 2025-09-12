import tensorflow as tf

# Sample vocabulary and corresponding embeddings
vocab = ['apple', 'banana', 'cherry', 'date']
embeddings = tf.constant([
    [0.1, 0.2, 0.3],
    [0.4, 0.5, 0.6],
    [0.7, 0.8, 0.9],
    [1.0, 1.1, 1.2]
], dtype=tf.float32)

# Create a mapping from vocabulary items to indices
vocab_to_index = tf.keras.layers.StringLookup(vocabulary=vocab, mask_token=None, oov_token='[UNK]')
vocab_to_index.set_vocabulary(vocab)

# Define a lookup function for embeddings
def lookup_embeddings(inputs):
    # Convert inputs to indices
    indices = vocab_to_index(inputs)
    
    # Check for invalid IDs or empty features and handle them
    valid_indices = tf.math.logical_and(indices >= 0, indices < tf.shape(embeddings)[0])
    indices = tf.where(valid_indices, indices, 0) # Map invalid/empty to index 0
    
    # Lookup embeddings
    result_embeddings = tf.nn.embedding_lookup(embeddings, indices)
    return result_embeddings

# Test Inputs
test_inputs = tf.constant(['apple', 'banana', 'invalid', ''], dtype=tf.string)

# Lookup Embeddings
embedding_results = lookup_embeddings(test_inputs)

# Display results
tf.print(embedding_results)
