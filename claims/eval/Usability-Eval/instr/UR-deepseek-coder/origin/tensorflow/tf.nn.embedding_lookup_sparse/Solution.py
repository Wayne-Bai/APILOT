import tensorflow as tf

def lookup_embeddings(embedding_matrix, ids, weights):
    """
    Looks up embeddings for the given ids and weights from a list of tensors.

    Args:
    embedding_matrix: A Tensor of shape [vocab_size, embedding_dim] containing the embedding vectors.
    ids: A Tensor of shape [batch_size, num_ids] containing the indices to look up.
    weights: A Tensor of shape [batch_size, num_ids] containing the weights for each id.

    Returns:
    A Tensor of shape [batch_size, embedding_dim] representing the weighted sum of the embeddings.
    """
    # Gather embeddings based on the ids
    embeddings = tf.nn.embedding_lookup(embedding_matrix, ids)
    
    # Expand dimensions of weights to match the shape of embeddings
    weights_expanded = tf.expand_dims(weights, axis=-1)
    
    # Perform element-wise multiplication of embeddings and weights
    weighted_embeddings = embeddings * weights_expanded
    
    # Sum the weighted embeddings along the num_ids dimension
    summed_embeddings = tf.reduce_sum(weighted_embeddings, axis=1)
    
    return summed_embeddings
