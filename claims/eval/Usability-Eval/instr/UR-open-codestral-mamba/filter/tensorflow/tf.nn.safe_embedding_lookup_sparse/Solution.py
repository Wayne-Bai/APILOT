import tensorflow as tf

def lookup_embedding_results_with_tensorflow(features, vocab_size, embedding_dim):
    # Initialize an embedding layer
    embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)

    # Convert the features to tensor format
    features_tensor = tf.convert_to_tensor(features)

    # Check if there are any invalid IDs (IDs that are greater than or equal to vocab_size)
    valid_ids = features_tensor < vocab_size

    # Create default embeddings for invalid IDs (e.g., all zeros)
    default_embeddings = tf.zeros([embedding_dim])

    # Replace the IDs that are greater than or equal to vocab_size with the default embeddings
    features_tensor = tf.where(valid_ids, features_tensor, default_embeddings)

    # Perform the embedding lookup
    embeddings = embedding(features_tensor)

    return embeddings

# Example usage
features = [1, 2, 3, 4, 5, 1000]  # Assume a vocab size of 1000
vocab_size = 1000
embedding_dim = 50

result = lookup_embedding_results_with_tensorflow(features, vocab_size, embedding_dim)
print(result)
