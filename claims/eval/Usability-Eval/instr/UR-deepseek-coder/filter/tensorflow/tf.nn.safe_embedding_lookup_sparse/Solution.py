import tensorflow as tf

def lookup_embedding(embedding_matrix, ids, invalid_id=-1, empty_feature_value=0.0):
    """
    Lookup embeddings for given IDs, handling invalid IDs and empty features.

    Args:
    embedding_matrix: A TensorFlow tensor representing the embedding matrix.
    ids: A TensorFlow tensor of IDs to lookup.
    invalid_id: The ID value that represents an invalid or missing ID.
    empty_feature_value: The value to use for features when the ID is invalid or missing.

    Returns:
    A TensorFlow tensor of embeddings corresponding to the given IDs, with invalid IDs handled.
    """
    # Create a mask for valid IDs
    valid_mask = tf.not_equal(ids, invalid_id)

    # Lookup embeddings for valid IDs
    embeddings = tf.nn.embedding_lookup(embedding_matrix, tf.where(valid_mask, ids, 0))

    # Create a tensor of empty feature values with the same shape as the embedding matrix
    empty_features = tf.fill(tf.shape(embedding_matrix)[1:], empty_feature_value)

    # Use tf.where to replace invalid embeddings with empty features
    result = tf.where(tf.expand_dims(valid_mask, axis=-1), embeddings, empty_features)

    return result

# Example usage:
# embedding_matrix = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
# ids = tf.constant([0, 1, -1, 2])
# result = lookup_embedding(embedding_matrix, ids)
# print(result.numpy())
