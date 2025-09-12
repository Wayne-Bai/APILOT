import tensorflow as tf

# Assuming you have a tensor 'ids' of shape (batch_size, seq_length) containing integer IDs
# and a tensor 'vocab_size' of shape (1,) containing the vocabulary size
# and a tensor 'embedding_dim' of shape (1,) containing the embedding dimension

# Create an embedding layer
embedding_layer = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=seq_length)

# Lookup embedding results, accounting for invalid IDs and empty features
def lookup_embedding(ids, embedding_layer):
    # Get the embedding for each ID in the 'ids' tensor
    embeddings = embedding_layer(ids)

    # Replace invalid IDs with zeros
    embeddings = tf.where(tf.equal(ids, 0), tf.zeros_like(embeddings), embeddings)

    # Replace empty features with zeros
    embeddings = tf.where(tf.equal(tf.reduce_sum(embeddings, axis=-1), 0), tf.zeros_like(embeddings), embeddings)

    return embeddings

# Example usage:
ids = tf.constant([[1, 2, 3], [4, 5, 6]])
embeddings = lookup_embedding(ids, embedding_layer)
print(embeddings)
