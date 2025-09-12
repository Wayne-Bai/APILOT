import tensorflow as tf

def lookup_embeddings(ids, weights, table):
    """
    Looks up embeddings for the given ids and weights from a list of tensors.

    Args:
        ids (tf.Tensor): A tensor of ids to look up.
        weights (tf.Tensor): A tensor of weights to apply to the embeddings.
        table (tf.Tensor): A tensor of embeddings to look up.

    Returns:
        tf.Tensor: A tensor of embeddings with the same shape as ids.
    """
    # Reshape the table tensor to have shape [num_embeddings, embedding_dim]
    table = tf.reshape(table, [-1, tf.shape(table)[-1]])

    # Lookup the embeddings for the given ids
    embeddings = tf.gather(table, ids)

    # Apply the weights to the embeddings
    embeddings = tf.reduce_sum(tf.multiply(embeddings, weights), axis=1)

    return embeddings
