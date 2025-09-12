import tensorflow as tf

def lookup_embeddings(embedding_matrix, ids, weights):
    """
    Looks up embeddings for the given ids and applies the corresponding weights.
    
    Parameters:
    - embedding_matrix: A tensor containing the embeddings.
    - ids: A list of ids to look up the embeddings for.
    - weights: A list of weights corresponding to each id.

    Returns:
    - A tensor containing the weighted sum of the embeddings.
    """
    # Convert ids and weights to tensors
    ids_tensor = tf.constant(ids, dtype=tf.int32)
    weights_tensor = tf.constant(weights, dtype=tf.float32)
    
    # Gather embeddings for the given ids
    selected_embeddings = tf.gather(embedding_matrix, ids_tensor)
    
    # Apply weights to the selected embeddings
    weighted_embeddings = selected_embeddings * tf.expand_dims(weights_tensor, axis=1)
    
    # Sum the weighted embeddings
    result = tf.reduce_sum(weighted_embeddings, axis=0)
    
    return result
