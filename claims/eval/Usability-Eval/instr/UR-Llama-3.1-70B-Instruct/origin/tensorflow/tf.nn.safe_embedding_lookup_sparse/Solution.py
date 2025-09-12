import tensorflow as tf

def safe_embedding_lookup(embedding, ids, num_valid_ids):
    """
    Lookup embedding results, accounting for invalid IDs and empty features.

    Args:
    - embedding: A 2D tensor representing the embedding matrix.
    - ids: A 2D tensor of type int32 containing the indices to look up.
    - num_valid_ids: The number of valid IDs in the 'ids' tensor.

    Returns:
    - looked_up_embedding: A 3D tensor representing the looked up embeddings.
    """
    max_id = tf.shape(embedding)[0] - 1

    # Mask out-of-range IDs
    clipped_ids = tf.clip_by_value(ids, 0, max_id)

    # Lookup the embeddings using the clipped IDs
    looked_up_embedding = tf.nn.embedding_lookup(embedding, clipped_ids)

    # Mask out embeddings for IDs that are out of range
    mask = tf.sequence_mask(num_valid_ids, tf.shape(looked_up_embedding)[1])
    looked_up_embedding = tf.where(mask, looked_up_embedding, tf.zeros_like(looked_up_embedding, dtype=tf.float32))

    return looked_up_embedding


# Example usage
if __name__ == "__main__":
    embedding = tf.random.uniform((10, 5))  # 10x5 embedding matrix
    ids = tf.constant([[0, 1, 10], [2, 3, 4]])  # 2x3 IDs tensor
    num_valid_ids = tf.constant([2, 3])  # Number of valid IDs in each row

    looked_up_embedding = safe_embedding_lookup(embedding, ids, num_valid_ids)

    with tf.Session() as sess:
        looked_up_embedding_result = sess.run(looked_up_embedding)
        print(looked_up_embedding_result)
