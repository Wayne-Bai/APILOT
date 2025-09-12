import tensorflow as tf

def get_embedding(embedding_matrix, ids, default_value=0.0):
    """
    Get embeddings for the given IDs, handling invalid IDs and empty features.

    Args:
    - embedding_matrix: A 2D tensor representing the embedding matrix.
    - ids: A 1D tensor of IDs for which to look up embeddings.
    - default_value: Default embedding value for invalid IDs.

    Returns:
    - A tensor of embeddings corresponding to the valid IDs.
    """
    
    # Check for empty features (IDs)
    if tf.size(ids) == 0:
        return tf.zeros([0, tf.shape(embedding_matrix)[1]])

    # Make sure IDs are valid and convert them to integer type
    ids = tf.cast(ids, tf.int32)

    # Mask for valid IDs
    valid_ids = tf.where(ids >= 0, ids, tf.cast(tf.fill(tf.shape(ids), -1), tf.int32))

    # Look up embeddings
    embeddings = tf.nn.embedding_lookup(embedding_matrix, valid_ids)

    # Create a mask to identify invalid IDs
    mask = tf.equal(valid_ids, -1)

    # Replace embeddings of invalid IDs with the default value
    invalid_embedding = tf.fill(tf.shape(embeddings)[1:], default_value)
    embeddings = tf.where(mask[:, tf.newaxis], invalid_embedding, embeddings)

    return embeddings
