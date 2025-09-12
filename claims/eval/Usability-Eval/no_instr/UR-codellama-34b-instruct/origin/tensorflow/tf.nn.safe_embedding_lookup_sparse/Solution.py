
import tensorflow as tf

# Define the embedding table and initializer
embedding_table = tf.get_variable(name="embeddings", shape=(1000, 50), initializer=tf.truncated_normal_initializer())

# Define a placeholder for the input IDs
input_ids = tf.placeholder(shape=[None], dtype=tf.int64)

# Define a mask to handle invalid IDs and empty features
mask = tf.cast(tf.not_equal(input_ids, 0), tf.bool)

# Perform the embedding lookup
embeddings = tf.nn.embedding_lookup(embedding_table, input_ids)

# Mask the invalid IDs and empty features
masked_embeddings = tf.where(mask, embeddings, 0.0)

# Print the result
print(masked_embeddings.eval())
