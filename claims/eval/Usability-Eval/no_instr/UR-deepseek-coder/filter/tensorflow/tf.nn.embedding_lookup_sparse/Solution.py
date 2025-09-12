import tensorflow as tf

def lookup_embeddings(ids, weights, embedding_matrix):
    """
    Looks up embeddings for the given ids and weights from a list of tensors.

    Args:
    ids: A list of tensors where each tensor contains the ids to be looked up.
    weights: A list of tensors where each tensor contains the corresponding weights.
    embedding_matrix: A tensor representing the embedding matrix.

    Returns:
    A tensor containing the weighted sum of the embeddings.
    """
    # Ensure the ids and weights lists have the same length
    if len(ids) != len(weights):
        raise ValueError("The lengths of ids and weights lists must be the same.")

    # Initialize a list to store the weighted embeddings
    weighted_embeddings = []

    # Loop through each set of ids and weights
    for i in range(len(ids)):
        # Gather the embeddings for the current ids
        embeddings = tf.nn.embedding_lookup(embedding_matrix, ids[i])

        # Apply the weights to the embeddings
        weighted_embedding = embeddings * tf.expand_dims(weights[i], axis=-1)

        # Append the weighted embeddings to the list
        weighted_embeddings.append(weighted_embedding)

    # Sum the weighted embeddings across all sets
    total_weighted_embedding = tf.reduce_sum(weighted_embeddings, axis=0)

    return total_weighted_embedding

# Example usage:
# embedding_matrix = tf.Variable(tf.random.normal([100, 32]))  # 100 embeddings of size 32
# ids = [tf.constant([1, 2, 3]), tf.constant([4, 5])]
# weights = [tf.constant([0.5, 0.3, 0.2]), tf.constant([0.7, 0.3])]
# result = lookup_embeddings(ids, weights, embedding_matrix)
