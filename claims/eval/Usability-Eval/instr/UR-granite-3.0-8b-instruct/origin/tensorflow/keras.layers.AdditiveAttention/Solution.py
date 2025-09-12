import tensorflow as tf

def additive_attention(query, values, attention_v, attention_weights=None):
    """
    This function implements the additive attention mechanism, also known as Bahdanau-style attention.

    Parameters:
    query (tf.Tensor): The query tensor of shape (batch_size, query_length, query_dim).
    values (tf.Tensor): The values tensor of shape (batch_size, max_length, value_dim).
    attention_v (tf.Tensor): The attention vector of shape (value_dim,).
    attention_weights (tf.Tensor, optional): The attention weights tensor of shape (batch_size, max_length). Default is None.

    Returns:
    tf.Tensor: The attention-weighted values tensor of shape (batch_size, query_length, value_dim).
    """
    # Calculate the attention scores
    attention_scores = tf.nn.tanh(query + tf.expand_dims(attention_v, 0))
    attention_scores = tf.reduce_sum(attention_scores * values, axis=-1)

    # Apply the attention weights (if provided)
    if attention_weights is not None:
        attention_scores += tf.expand_dims(attention_weights, -1)

    # Apply the softmax function to get the attention weights
    attention_weights = tf.nn.softmax(attention_scores, axis=-1)

    # Calculate the attention-weighted values
    attention_weighted_values = tf.reduce_sum(attention_weights * values, axis=-2)

    return attention_weighted_values
