import tensorflow as tf

def lookup_embedding(embedding_matrix, ids, default_embedding):
    """
    Lookup embeddings by ids, handle invalid ids by providing a default embedding.

    Args:
    - embedding_matrix (tf.Tensor): The tensor containing the embeddings.
    - ids (tf.Tensor): The tensor containing the IDs to lookup in the embedding matrix.
    - default_embedding (tf.Tensor): The tensor to use for invalid or not-found IDs.

    Returns:
    - tf.Tensor: The tensor with the resulting embeddings.
    """
    embedding_dim = embedding_matrix.shape[1]
    max_id = tf.shape(embedding_matrix)[0] - 1

    # Use tf.clip_by_value to ensure ids are within valid range
    clipped_ids = tf.clip_by_value(ids, 0, max_id)

    # Gather embeddings with clipped ids
    selected_embeddings = tf.gather(embedding_matrix, clipped_ids)

    # Create a mask for invalid ids
    valid_ids = tf.logical_and(ids >= 0, ids <= max_id)
    valid_mask = tf.expand_dims(valid_ids, -1)

    # Cast mask to the same dtype as embeddings
    valid_mask = tf.cast(valid_mask, selected_embeddings.dtype)

    # Use mask to select between selected_embeddings and default_embedding
    result_embeddings = tf.where(valid_mask, selected_embeddings, default_embedding)

    return result_embeddings

# Example usage:
# Assuming embeddings matrix is of shape (num_embeddings, embedding_dim), ids is the tensor of item IDs
embedding_dim = 5
num_embeddings = 10
default_embedding = tf.zeros((1, embedding_dim))

# Random example embedding matrix
np.random.seed(0)
example_embeddings = tf.convert_to_tensor(np.random.rand(num_embeddings, embedding_dim), dtype=tf.float32)

# Example IDs (including out-of-range values to demonstrate handling)
example_ids = tf.convert_to_tensor([0, 5, 10, 15, -1], dtype=tf.int32)

# Get the output embeddings
output_embeddings = lookup_embedding(example_embeddings, example_ids, default_embedding)
print("Output Embeddings:\n", output_embeddings)
