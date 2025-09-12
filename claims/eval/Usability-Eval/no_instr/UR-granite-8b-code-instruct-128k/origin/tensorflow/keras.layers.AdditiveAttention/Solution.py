import tensorflow as tf

def additive_attention(query, values, key_mask=None):
    query_shape = tf.shape(query)
    values_shape = tf.shape(values)
    attention_input = tf.concat([query, values], axis=-1)
    attention_scores = tf.reduce_sum(tf.tanh(attention_input) * attention_input, axis=-1, keepdims=True)
    attention_scores = tf.exp(attention_scores)
    if key_mask is not None:
        key_mask = tf.expand_dims(key_mask, axis=1)
        attention_scores = attention_scores * key_mask
    attention_scores = attention_scores / tf.reduce_sum(attention_scores, axis=-1, keepdims=True)
    context_vector = tf.reduce_sum(attention_scores * values, axis=1)

    return context_vector
