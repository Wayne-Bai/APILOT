import tensorflow as tf

def dot_product_attention(query, key, value, mask=None):
    # Scale query and key by sqrt(d_k)
    d_k = tf.cast(tf.shape(query)[-1], tf.float32)
    scale_query = tf.math.rsqrt(d_k)
    scale_key = tf.math.rsqrt(d_k)
    query = query * scale_query
    key = key * scale_key

    # Calculate attention scores
    scores = tf.matmul(query, key, transpose_b=True)

    # Apply mask if provided
    if mask is not None:
        scores += (mask * -1e9)

    # Softmax along the last dimension
    attention_weights = tf.nn.softmax(scores, axis=-1)

    # Calculate the weighted sum of values
    output = tf.matmul(attention_weights, value)

    return output
