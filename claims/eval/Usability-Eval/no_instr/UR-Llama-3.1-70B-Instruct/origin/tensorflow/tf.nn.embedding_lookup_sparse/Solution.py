import tensorflow as tf

def lookup_embeddings(ids, weights, embedding_tables):
    """
    Looks up embeddings for the given ids and weights from a list of embedding tables.

    Args:
    ids (list): A list of ids to look up in the embedding tables.
    weights (list): A list of weights to apply to the embeddings.
    embedding_tables (list): A list of embedding tables.

    Returns:
    A tensor of embeddings with shape (len(ids), embedding_dim).
    """
    # Create a tensor from the ids
    ids_tensor = tf.constant(ids)

    # Create a tensor from the weights
    weights_tensor = tf.constant(weights)

    # Initialize an empty tensor to store the embeddings
    embeddings = []

    # Iterate over the embedding tables
    for i, embedding_table in enumerate(embedding_tables):
        # Look up the embeddings for the current ids in the current embedding table
        embedding = tf.gather(embedding_table, ids_tensor, axis=0)

        # Apply the weights to the embeddings
        weighted_embedding = embedding * weights_tensor[:, tf.newaxis]

        # Add the weighted embeddings to the list
        embeddings.append(weighted_embedding)

    # Stack the embeddings into a single tensor
    embeddings = tf.stack(embeddings, axis=0)

    # Sum the embeddings along the first axis
    embeddings = tf.reduce_sum(embeddings, axis=0)

    return embeddings


# Example usage
ids = [1, 2, 3]
weights = [0.2, 0.3, 0.5]
embedding_tables = [
    tf.constant([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]),
    tf.constant([[0.7, 0.8], [0.9, 1.0], [1.1, 1.2]])
]

output = lookup_embeddings(ids, weights, embedding_tables)
print(output)
