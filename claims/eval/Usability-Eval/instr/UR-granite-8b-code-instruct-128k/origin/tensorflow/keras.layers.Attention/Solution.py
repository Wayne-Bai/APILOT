import tensorflow as tf
def dot_product_attention(queries, keys, values, mask):
    matmul = tf.matmul(queries, keys, transpose_b=True)
    if mask is not None:
        matmul = matmul + mask * (-1e9)
    attention = tf.nn.softmax(matmul, axis=-1)
    output = tf.matmul(attention, values)
    return output
