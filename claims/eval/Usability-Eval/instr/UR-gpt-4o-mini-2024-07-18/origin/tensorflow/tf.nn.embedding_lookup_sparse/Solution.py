import tensorflow as tf

def lookup_embeddings(ids, weights, embeddings):
    """
    Lookup embeddings for the given ids and applies weights.

    Args:
        ids (tf.Tensor): A tensor of IDs to look up.
        weights (tf.Tensor): A tensor of weights corresponding to the IDs.
        embeddings (tf.Tensor): A tensor containing the embeddings.

    Returns:
        tf.Tensor: A tensor of weighted embeddings.
    """
    # Gather the embeddings for the given ids
    selected_embeddings = tf.gather(embeddings, ids)
    
    # Element-wise multiplication of the selected embeddings with weights
    weighted_embeddings = selected_embeddings * tf.expand_dims(weights, axis=-1)
    
    return weighted_embeddings

# Example usage
if __name__ == "__main__":
    # Sample data
    embeddings = tf.constant([[1.0, 2.0, 3.0],
                              [4.0, 5.0, 6.0],
                              [7.0, 8.0, 9.0]], dtype=tf.float32)
    
    ids = tf.constant([1, 2], dtype=tf.int32)
    weights = tf.constant([0.5, 2.0], dtype=tf.float32)
    
    # Lookup embeddings
    result = lookup_embeddings(ids, weights, embeddings)
    print(result.numpy())  # Output the result
