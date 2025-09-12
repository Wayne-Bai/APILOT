import tensorflow as tf

# Inputs
queries = tf.placeholder(tf.float32, shape=[None, None])
keys = tf.placeholder(tf.float32, shape=[None, None])
values = tf.placeholder(tf.float32, shape=[None, None])
attention_mask = tf.placeholder(tf.float32, shape=[None, None])

# Compute dot product attention score
query = tf.reshape(queries, [-1, 1, 1, None])
key = tf.reshape(keys, [-1, None, 1, None])
dot_product = tf.matmul(query, key, transpose_a=True)
attention_score = dot_product / math.sqrt(keys.shape[-1].value)
attention_score = attention_score + attention_mask
attention_weights = tf.nn.softmax(attention_score, axis=-1)

# Compute weighted sum of values using attention weights
weighted_sum = tf.matmul(values, attention_weights)
