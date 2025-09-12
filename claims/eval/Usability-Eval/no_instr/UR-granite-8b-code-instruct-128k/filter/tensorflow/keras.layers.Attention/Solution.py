import tensorflow as tf

def dot_product_attention(queries, keys, values, mask):
    matmul = tf.matmul(queries, keys, transpose_b=True)
    scaled_matmul = matmul * (1.0 / tf.sqrt(tf.cast(tf.shape(keys)[-1], tf.float32)))
    if mask is not None:
        scaled_matmul += mask * (-1e9)
    attention_weights = tf.nn.softmax(scaled_matmul, axis=-1)
    attention_output = tf.matmul(attention_weights, values)
    return attention_output
