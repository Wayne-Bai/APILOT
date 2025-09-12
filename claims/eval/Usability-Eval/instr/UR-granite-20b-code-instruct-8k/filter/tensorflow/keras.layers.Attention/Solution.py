import tensorflow as tf

def dot_product_attention(Q, K, V):
    # calculate the matrix multiplication of Q and K
    # and then compute the softmax of the result
    attention_weights = tf.nn.softmax(tf.matmul(Q, K, transpose_b=True))
    # calculate the matrix multiplication of attention_weights
    # and V to get the final output
    output = tf.matmul(attention_weights, V)
    return output
