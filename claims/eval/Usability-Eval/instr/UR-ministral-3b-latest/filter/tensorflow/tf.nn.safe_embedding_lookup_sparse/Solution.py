import tensorflow as tf

# Assuming inputs are 'embedding_ids' and 'Athletes' are your features, and 'embedding_lookup' is your desired embedding result.
def lookup_embedding_results(embedding_ids, Athletes, embedding_lookup):
    # Adding a check to handle invalid IDs
    valid_ids = [id_ for id_ in embedding_ids if 0 <= id_ < embedding_lookup.embedding_matrix.shape[0]]

    # Handling empty features
    valid_features = [feature for feature in Athletes if feature is not None]

    valid_embedding_ids = valid_ids[:len(valid_features)]

    # Extract the corresponding embeddings for the valid IDs
    valid_embeddings = embedding_lookup((valid_embedding_ids[tf.newaxis, :],), data_format="tf", stable=False)

    # Since you wanted to process the results in the context of empty features, we handle it here by initializing an empty list,
    # then appending the corresponding features with the valid embeddings:
    embedding_results = []
    for idx, feature in enumerate(valid_features):
        embedding_results.append(valid_embeddings[0][idx])

    # Returning all valid embeddings
    return tf.constant(valid_embedding_ids), tf.constant(valid_embeddings[0]), tf.convert_to_tensor(embedding_results)

# Example usage
# embedding_lookup is an instance with embedding_matrix, e.g., tf.keras.layers.Embedding()
# embedding_lookup = tf.keras.layers.Embedding(100, 8, embeddings_initializer="uniform")
# embedding_ids = [1, 2, 3, 6, 99, 200]  # Example IDs
# valid_features = [' valid feature 1', None, 'valid feature 2', 'valid feature 3']  # Example features with some None values

# valid_ids_tensor, valid_embedding_tensor, valid_results = lookup_embedding_results(embedding_ids, valid_features, embedding_lookup)
