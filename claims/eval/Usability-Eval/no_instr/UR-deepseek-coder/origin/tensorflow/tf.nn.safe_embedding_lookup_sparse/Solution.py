import tensorflow as tf

def lookup_embedding(embedding_matrix, ids, default_value=0.0):
    """
    Lookup embedding results, accounting for invalid IDs and empty features.

    Args:
    embedding_matrix: A TensorFlow Variable representing the embedding matrix.
    ids: A TensorFlow Tensor containing the IDs to lookup.
    default_value: The default value to use for invalid IDs.

    Returns:
    A TensorFlow Tensor containing the embedding results.
    """
    # Ensure the embedding matrix is a Variable
    if not isinstance(embedding_matrix, tf.Variable):
        raise ValueError("embedding_matrix must be a TensorFlow Variable")

    # Ensure the ids are a Tensor
    if not isinstance(ids, tf.Tensor):
        raise ValueError("ids must be a TensorFlow Tensor")

    # Create a mask for valid IDs
    valid_mask = tf.greater(ids, -1)

    # Convert ids to int32 if they are not already
    ids = tf.cast(ids, tf.int32)

    # Gather embeddings using the valid IDs
    embeddings = tf.gather(embedding_matrix, ids)

    # Create a tensor of default values with the same shape as embeddings
    default_embeddings = tf.fill(tf.shape(embeddings), default_value)

    # Use the mask to select either the gathered embeddings or the default values
    result = tf.where(valid_mask, embeddings, default_embeddings)

    return result

# Example usage:
# embedding_matrix = tf.Variable(tf.random.normal([100, 64]))  # 100 embeddings of size 64
# ids = tf.constant([0, 1, -1, 3, -1])  # Example IDs with invalid IDs (-1)
# embeddings = lookup_embedding(embedding_matrix, ids)
