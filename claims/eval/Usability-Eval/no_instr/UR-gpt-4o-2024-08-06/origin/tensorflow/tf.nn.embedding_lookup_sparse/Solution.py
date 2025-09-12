import tensorflow as tf

# Create a simple embeddings matrix
embedding_matrix = tf.constant([
    [0.0, 0.1, 0.2],
    [0.3, 0.4, 0.5],
    [0.6, 0.7, 0.8],
    [0.9, 1.0, 1.1]
])

# Define the IDs for which we want to retrieve embeddings
ids = tf.constant([0, 2, 3], dtype=tf.int32)

# Define weights for each id to scale embeddings
weights = tf.constant([0.5, 1.5, 1.0], dtype=tf.float32)

# Look up multiple embeddings; this is similar to tf.nn.embedding_lookup
embeddings = tf.gather(embedding_matrix, ids)

# Scale embeddings based on the weights
weighted_embeddings = embeddings * tf.expand_dims(weights, 1)

# Sum the weighted embeddings
result = tf.reduce_sum(weighted_embeddings, axis=0)

print("Embeddings Matrix:")
print(embedding_matrix.numpy())

print("\nSelected IDs:")
print(ids.numpy())

print("\nWeights:")
print(weights.numpy())

print("\nSelected Embeddings:")
print(embeddings.numpy())

print("\nWeighted Embeddings:")
print(weighted_embeddings.numpy())

print("\nFinal Weighted Sum of Embeddings:")
print(result.numpy())
