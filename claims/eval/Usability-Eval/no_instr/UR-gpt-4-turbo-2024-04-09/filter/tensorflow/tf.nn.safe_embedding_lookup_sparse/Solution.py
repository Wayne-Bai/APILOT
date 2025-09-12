import tensorflow as tf

def lookup_embeddings(features, embedding_matrix, invalid_id=-1):
    """
    Lookup embedding results, replacing invalid IDs with a zero embedding.

    Args:
    features: A Tensor containing integer IDs that index into the `embedding_matrix`.
    embedding_matrix: A 2D Tensor containing the embeddings.
    invalid_id: An integer representing an ID that should be treated as invalid (defaults to -1).

    Returns:
    A Tensor containing the embeddings corresponding to the features.
    """
    num_embeddings, embedding_dim = embedding_matrix.shape
    # Create a mask for valid IDs
    valid_mask = tf.not_equal(features, invalid_id)

    # Handle the case where features might be an empty tensor
    if features.shape[0] == 0:
        return tf.zeros([0, embedding_dim], dtype=embedding_matrix.dtype)

    # Zero embedding for the invalid ID
    zero_embedding = tf.zeros([1, embedding_dim], dtype=embedding_matrix.dtype)

    # Concatenate the zero embedding to handle invalid IDs
    embedding_matrix_extended = tf.concat([embedding_matrix, zero_embedding], axis=0)

    # Adjust invalid IDs to index the last row (zero embedding)
    features_safe = tf.where(valid_mask, features, tf.constant(num_embeddings, dtype=features.dtype))

    # Lookup embeddings
    embeddings = tf.gather(embedding_matrix_extended, features_safe)

    return embeddings

# Example usage
# Pseudo-random embeddings and sample feature IDs (including an invalid ID -1)
embedding_matrix_example = tf.random.uniform([10, 5], minval=-1, maxval=1)  # 10 embeddings, 5 dimensions each
features_example = tf.constant([1, 3, -1, 5, 8])  # Feature IDs (with -1 as invalid)

# Get the embeddings
embeddings_result = lookup_embeddings(features_example, embedding_matrix_example)
print("Embeddings Result:")
print(embeddings_result)
