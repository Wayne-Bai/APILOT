import tensorflow as tf

def lookup_embeddings(ids, weights, embedding_table):
    """
    This function looks up embeddings for the given ids and weights from a list of tensors.

    Args:
    ids (tf.Tensor): A tensor of ids to look up embeddings for.
    weights (tf.Tensor): A tensor of weights to apply to the embeddings.
    embedding_table (tf.Tensor): A tensor of embeddings to look up.

    Returns:
    tf.Tensor: A tensor of embeddings with the same shape as weights.
    """
    # Flatten the weights tensor to apply the weights to each embedding individually
    flattened_weights = tf.reshape(weights, [-1])

    # Look up the embeddings for each id in the ids tensor
    embeddings = tf.gather(embedding_table, ids)

    # Apply the weights to each embedding individually
    weighted_embeddings = embeddings * flattened_weights

    # Reshape the weighted embeddings tensor to match the shape of the weights tensor
    weighted_embeddings = tf.reshape(weighted_embeddings, weights.shape)

    return weighted_embeddings
