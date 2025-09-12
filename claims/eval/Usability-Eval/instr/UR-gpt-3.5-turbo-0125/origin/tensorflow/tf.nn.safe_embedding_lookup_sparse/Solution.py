
import tensorflow as tf

def lookup_embedding_safe(embedding_matrix, feature_ids):
    # Find invalid IDs (those that are out of range)
    max_id = tf.shape(embedding_matrix)[0]
    valid_ids = tf.boolean_mask(feature_ids, tf.less(feature_ids, max_id))

    # Replace invalid IDs with an index pointing to a default embedding (e.g. first row of the embedding matrix)
    default_embedding_index = tf.zeros_like(valid_ids)
    safe_feature_ids = tf.where(tf.less(feature_ids, max_id), feature_ids, default_embedding_index)

    # Lookup embeddings for valid and safe feature IDs
    embeddings = tf.nn.embedding_lookup(embedding_matrix, safe_feature_ids)

    return embeddings

# Example usage
embedding_matrix = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
feature_ids = tf.constant([1, 3, 0, 5])

result = lookup_embedding_safe(embedding_matrix, feature_ids)
