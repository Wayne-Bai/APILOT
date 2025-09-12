import tensorflow as tf

def embeddings_lookup_sparse(params, sp_ids, sp_weights, combiner):
    """Looks up embeddings for the given ids and weights from a list of tensors."""
    return tf.nn.embedding_lookup_sparse(params, sp_ids, sp_weights, combiner)
