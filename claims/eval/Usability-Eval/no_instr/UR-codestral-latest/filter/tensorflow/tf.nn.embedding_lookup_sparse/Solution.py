import tensorflow as tf

def lookup_embeddings(ids, weights, embeddings):
    """
    This function looks up embeddings for the given ids and weights from a list of embeddings.
    :param ids: A tensor with shape [batch_size] containing the ids to be looked up.
    :param weights: A tensor with shape [batch_size, num_features] containing the weight of each feature.
    :param embeddings: A list of tensors where each tensor has shape [vocab_size, embedding_dim].
    :return: A tensor with shape [batch_size, embedding_dim] containing the resulting embeddings.
    """
    # Initialize a zeros tensor to store the result
    result = tf.zeros([tf.shape(ids)[0], embeddings[0].shape[1]])

    # Lookup the embeddings and weighted average them
    for i in range(len(embeddings)):
        embedding_i = tf.nn.embedding_lookup(embeddings[i], ids)
        weight_i = tf.expand_dims(weights[:, i], axis=-1)
        result += weight_i * embedding_i

    return result
