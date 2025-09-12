import tensorflow as tf

def dot_product_attention(q, k, v, mask=None):
    # Calculate the dot product of the query with all the keys
    dot_product = tf.matmul(q, k, transpose_b=True)

    # Scale the dot product by the square root of the key vector dimension
    scale = tf.math.sqrt(tf.cast(tf.shape(k)[-1], tf.float32))
    dot_product = dot_product / scale

    # Apply the softmax function to get the attention weights
    if mask is not None:
        dot_product = tf.where(mask, dot_product, -1e9)  # Set the mask values to a large negative number
    attention_weights = tf.nn.softmax(dot_product, axis=-1)

    # Calculate the weighted sum of the values using the attention weights
    output = tf.matmul(attention_weights, v)

    return output
