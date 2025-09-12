import tensorflow as tf

def lookup_embedding(ids, vocab_size, embedding_dim, default_value=None):
    """
    Look up embedding results, accounting for invalid IDs and empty features.

    Args:
        ids (tf.Tensor): Tensor of IDs to look up embeddings for.
        vocab_size (int): Size of the vocabulary.
        embedding_dim (int): Dimensionality of the embeddings.
        default_value (tf.Tensor, optional): Default value to use for invalid IDs. Defaults to None.

    Returns:
        tf.Tensor: Tensor of embedding results.
    """
    # Create an embedding lookup table
    embedding_table = tf.Variable(tf.random.uniform([vocab_size, embedding_dim]))

    # Look up embeddings for valid IDs
    valid_ids = tf.gather(embedding_table, ids)

    # Replace invalid IDs with default value
    if default_value is not None:
        invalid_ids = tf.boolean_mask(ids, tf.equal(ids, -1))
        invalid_ids = tf.ragged.constant([invalid_ids])
        invalid_ids = tf.squeeze(invalid_ids)
        invalid_ids = tf.ragged.boolean_mask(invalid_ids, tf.zeros_like(invalid_ids))
        invalid_ids = tf.ragged.flatten(invalid_ids)
        invalid_ids = tf.gather(default_value, invalid_ids)
        valid_ids = tf.concat([valid_ids, invalid_ids], axis=0)

    return valid_ids
