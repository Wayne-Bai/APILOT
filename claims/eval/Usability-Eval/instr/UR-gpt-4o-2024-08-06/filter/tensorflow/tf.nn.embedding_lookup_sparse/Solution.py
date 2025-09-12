import tensorflow as tf

# Create some sample data
embeddings = tf.constant([
    [1.0, 2.0],
    [3.0, 4.0],
    [5.0, 6.0],
    [7.0, 8.0]
], dtype=tf.float32)

# Sample ids and weights
ids = tf.constant([0, 2, 1, 3], dtype=tf.int32)
weights = tf.constant([0.1, 0.6, 0.2, 0.1], dtype=tf.float32)

# Lookup embeddings using ids
selected_embeddings = tf.nn.embedding_lookup(params=embeddings, ids=ids)

# Multiply each embedding by the respective weight
weighted_embeddings = selected_embeddings * tf.expand_dims(weights, 1)

# Display the resulting embeddings
print(weighted_embeddings.numpy())
